from django.forms import ModelForm, CharField
from task_manager.tools import gettext_lazy
from .models import Status


class StatusForm(ModelForm):
    name = CharField(
        max_length=100,
        required=True,
        label=gettext_lazy('Name')
    )

    class Meta:
        model = Status
        fields = ('name', )
