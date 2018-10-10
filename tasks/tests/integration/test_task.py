import pytest
from rest_framework.test import APIRequestFactory
from tasks.api.views.task import (
    MissionTasksList, TaskDetail
)


@pytest.mark.django_db
def test_task_list(setup_task):
    factory = APIRequestFactory()

    # Task list
    mission_id = 1
    request = factory.get('/api/v1/missions/{0}/tasks'.format(mission_id))
    view = MissionTasksList.as_view()
    response = view(request, mission_id)
    assert response.status_code == 200
    assert response.data == [
        {'id': 1, 'name': 'Add two digits', 'description': ''}
    ]

    # Task empty list
    mission_id = 2
    request = factory.get('/api/v1/missions/{0}/tasks'.format(mission_id))
    view = MissionTasksList.as_view()
    response = view(request, mission_id)
    assert response.status_code == 200
    assert response.data == []

    request = factory.get('/api/v1/missions/{0}/tasks'.format(100))
    view = MissionTasksList.as_view()
    response = view(request, 100)
    assert response.status_code == 404
    assert response.data["detail"].code == "not_found"


@pytest.mark.django_db
def test_task_details(setup_task):
    factory = APIRequestFactory()

    # Task details
    task_id = 1
    request = factory.get('/tasks/{0}'.format(task_id))
    view = TaskDetail.as_view()
    response = view(request, task_id)
    assert response.status_code == 200
    assert response.data == {'id': 1, 'name': 'Add two digits', 'description': ''}

    # Task details, task not found
    request = factory.get('/tasks/{0}'.format(100))
    view = TaskDetail.as_view()
    response = view(request, 100)
    assert response.status_code == 404
    assert response.data["detail"].code == "not_found"
