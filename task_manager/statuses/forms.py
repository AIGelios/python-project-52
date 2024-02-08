from django.forms import ModelForm, CharField
from task_manager import gettext_lazy
from .models import Status


class StatusForm(ModelForm):
    name = CharField(
        max_length=255,
        required=True,
        label=gettext_lazy('Name')
    )

    class Meta:
        model = Status
        fields = ('name', )
