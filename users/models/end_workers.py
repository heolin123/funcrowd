from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

from funcrowd.settings import events_manager
from modules.achievements.events import Events
from modules.statistics.models import UserStats, UserMissionStats
from users.consts import ProfileType
from users.models.manager import EndWorkerManager
from users.models.storage import Storage
from users.models.utils.utils import get_group_number
from django.utils.translation import ugettext_lazy as _


import tasks as t


class EndWorker(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    group = models.IntegerField(default=get_group_number)
    profile = models.IntegerField(default=ProfileType.NORMAL)

    login_count = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    level = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = EndWorkerManager()

    @property
    def token(self):
        result, _ = Token.objects.get_or_create(user=self)
        return result

    @property
    def stats(self):
        stats, _ = UserStats.objects.get_or_create(user=self)
        return stats

    def create_activation_token(self):
        from users.models import ActivationToken
        for token in ActivationToken.objects.filter(user=self):
            token.token_used = True
            token.save()
        return ActivationToken.objects.create(user=self)

    def create_password_token(self):
        from users.models import PasswordToken
        for token in PasswordToken.objects.filter(user=self):
            token.token_used = True
            token.save()
        return PasswordToken.objects.create(user=self)

    def get_storage(self, key):
        storage = Storage.objects.filter(user=self, key=key).first()
        if not storage:
            storage = Storage.objects.create(user=self, key=key)
        return storage

    def set_storage(self, key, data):
        storage = self.get_storage(key)
        storage.data = data
        storage.save()

    def get_task_progress(self, task):
        # move this part to Task
        progress, _ = t.models.task_progress.UserTaskProgress.objects.get_or_create(
            task=task, user=self)
        progress.update_status()
        return progress

    def get_mission_stats(self, mission_id):
        # move this part to Mission
        stats, _ = UserMissionStats.objects.get_or_create(user=self, mission_id=mission_id)
        return stats

    def get_mission_progress(self, mission):
        # move this part to Mission
        progress, _ = t.models.mission_progress.UserMissionProgress.objects.get_or_create(
            mission=mission, user=self)
        progress.update_status()
        return progress

    def on_login(self):
        self.login_count += 1
        self.save()
        events_manager.update_all(self)

    def on_annotation(self, annotation):
        task_progress = self.get_task_progress(annotation.item.task)
        task_progress.update()

        mission_progress = self.get_mission_progress(annotation.item.task.mission)
        mission_progress.update()

        if annotation.item.package:
            package_progress = annotation.item.package.get_user_progress(self)
            package_progress.update()

        events_manager.on_event(self, Events.ON_ITEM_DONE)

    def add_exp(self, exp):
        self.exp += exp
        self.save()


