from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField,
    ForeignKey,
    PROTECT,
)
from task_manager.apps.users.models import User
from task_manager.apps.statuses.models import Status


class Task(Model):
    name = CharField(max_length=400)
    created_at = DateTimeField(auto_now_add=True)
    description = TextField(max_length=16384)
    author = ForeignKey(
        to=User,
        on_delete=PROTECT,
        blank=False,
        null=False,
        related_name='task_author',
    )
    performer = ForeignKey(
        to=User,
        on_delete=PROTECT,
        blank=True,
        null=True,
        related_name='task_performer',
    )
    status = ForeignKey(
        to=Status,
        on_delete=PROTECT,
        blank=False,
        null=True
    )
