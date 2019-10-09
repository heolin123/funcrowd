# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.db.models import IntegerField
from django.db.models.functions import Cast, Coalesce
from django.contrib.postgres.fields import JSONField
from tasks.models.mission import Mission

from modules.order_strategy.models import Strategy
import modules.achievements as a


"""
Tasks are the base object for core logic of the platform
"""


class Task(models.Model):
    name = models.CharField(max_length=300)
    keywords = models.CharField(max_length=100, default="", blank=True)
    description = models.CharField(max_length=500, default="", blank=True)
    instruction = models.TextField(default="", blank="")
    created = models.DateTimeField(auto_now_add=True)

    metadata = JSONField(blank=True, default={})

    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name="tasks")
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)

    max_annotations = models.IntegerField(default=0)
    multiple_annotations = models.BooleanField(default=False)

    order = models.IntegerField(default=0)

    def next_item(self, user, item):
        return self.strategy.next(self, user, item)

    def prev_item(self, user, item):
        return self.strategy.prev(self, user, item)

    def exclude_items_with_user_annotations(self, user):
        return self.items.exclude(annotations__user=user, annotations__annotated=True)

    def annotate_annotations_done(self, items):
        return items.annotate(annotations_done=models.Sum(
            Coalesce(Cast('annotations__annotated', IntegerField()), 0)))

    def exclude_max_annotations(self, items):
        return items.filter(annotations_done__lt=self.max_annotations)

    @property
    def achievements_count(self):
        cls = a.models.Achievement
        return cls.objects.filter(task=self).count()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return "{}({})".format(
            self.__class__.__name__,
            'name='+self.name,
        )
