import pytest

from tasks.models import Task
from modules.quality_control.models import AgreementMetric
from modules.quality_control.exceptions import MultipleTempaltesFound


@pytest.mark.django_db
def test_one_field(setup_task_one_variable):
    task = Task.objects.first()
    scotts_pi, _ = AgreementMetric.objects.get_or_create(name="ScottsPiMetric")
    for metric in scotts_pi.evaluate(task):
        assert metric.name == "ScottsPiMetric"
        assert metric.column == "output"
        assert round(metric.value, 2) == 0.21


@pytest.mark.django_db
def test_high_agreement(setup_task_high_agreement):
    task = Task.objects.first()
    scotts_pi, _ = AgreementMetric.objects.get_or_create(name="ScottsPiMetric")
    for metric in scotts_pi.evaluate(task):
        assert metric.name == "ScottsPiMetric"
        assert metric.column == "output"
        assert round(metric.value, 2) == 0.64


@pytest.mark.django_db
def test_multiple_templates(setup_task_multiple_templates):
    task = Task.objects.first()
    scotts_pi, _ = AgreementMetric.objects.get_or_create(name="ScottsPiMetric")
    with pytest.raises(MultipleTempaltesFound):
        scotts_pi.evaluate(task)


@pytest.mark.django_db
def test_two_fields(setup_task_two_variables):
    task = Task.objects.first()
    scotts_pi, _ = AgreementMetric.objects.get_or_create(name="ScottsPiMetric")
    for metric, column in zip(scotts_pi.evaluate(task), ["output1", "output2"]):
        assert metric.name == "ScottsPiMetric"
        assert metric.column == column
        assert round(metric.value, 2) == 0.21


@pytest.mark.django_db
def test_missing_data(setup_task_missing_data):
    task = Task.objects.first()
    scotts_pi, _ = AgreementMetric.objects.get_or_create(name="ScottsPiMetric")

    logic = scotts_pi._logic(task)
    logic.df["output"] = logic.df["data"].apply(lambda x: x["output"])
    counts = logic._get_pivot_table_counts("output")
    assert len(counts) == 9

    for metric in scotts_pi.evaluate(task):
        assert metric.name == "ScottsPiMetric"
        assert metric.column == "output"
        assert round(metric.value, 2) == 0.18


