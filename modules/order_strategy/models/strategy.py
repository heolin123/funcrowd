# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from .logic import STRATEGY_LOGICS


class Strategy(models.Model):
    name = models.CharField(max_length=30)

    @property
    def _logic(self):
        return STRATEGY_LOGICS[self.name]

    def next(self, task, user, item):
        return self._logic(task, user, item).next()

    def prev(self, task, user, item):
        return self._logic(task, user, item).prev()

    class Meta:
        verbose_name_plural = "Strategies"

    def __str__(self):
        return "{}({})".format(
            self.__class__.__name__,
            'name='+self.name,
        )

    def save(self, *args, **kwargs):
        objects = self.__class__.objects.filter(name=self.name)
        if objects:
            self.pk = objects.first().pk
        super().save(*args, **kwargs)

    @staticmethod
    def register_values():
        # register all strategy
        for strategy_name in STRATEGY_LOGICS:
            Strategy.objects.get_or_create(name=strategy_name)
