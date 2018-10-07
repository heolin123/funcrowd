# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from .logic import STRATEGY_LOGICS


class Strategy(models.Model):
    name = models.CharField(max_length=30)

    def _logic(self, task, user, item):
        return STRATEGY_LOGICS[self.name](task, user, item)

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

    @staticmethod
    def register_values():
        # register all strategy
        for strategy_name in STRATEGY_LOGICS:
            Strategy.objects.get_or_create(name=strategy_name)
