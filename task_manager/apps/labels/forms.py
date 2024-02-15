from django.forms import ModelForm, CharField
from task_manager.apps.tools import gettext_lazy
from .models import Label


class LabelForm(ModelForm):
    name = CharField(
        max_length=100,
        required=True,
        label=gettext_lazy('Name')
    )

    class Meta:
        model = Label
        fields = ('name', )
