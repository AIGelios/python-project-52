from django.db.models import (
    Model, CharField, TextField, DateTimeField,
    ForeignKey, ManyToManyField, PROTECT, CASCADE,
)
from task_manager.apps.users.models import User
from task_manager.apps.statuses.models import Status
from task_manager.apps.labels.models import Label


class Task(Model):
    name = CharField(max_length=150)
    created_at = DateTimeField(auto_now_add=True)
    description = TextField(max_length=16384)
    author = ForeignKey(
        to=User,
        on_delete=PROTECT,
        blank=False,
        null=False,
        related_name='task_author',
    )
    executor = ForeignKey(
        to=User,
        on_delete=PROTECT,
        blank=True,
        null=True,
        related_name='task_executor',
    )
    status = ForeignKey(
        to=Status,
        on_delete=PROTECT,
        blank=False,
        null=True
    )
    label = ManyToManyField(
        to=Label,
        through='TaskLabel',
        blank=True
    )

    def __str__(self):
        return self.name


class TaskLabel(Model):
    task = ForeignKey(to=Task, on_delete=CASCADE)
    label = ForeignKey(to=Label, on_delete=PROTECT)
