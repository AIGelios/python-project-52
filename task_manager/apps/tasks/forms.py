from task_manager.tools import gettext_lazy
from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'status',
            'executor',
            'labels',
        )
        labels = dict(
            name=gettext_lazy('Name'),
            description=gettext_lazy('Description'),
            status=gettext_lazy('Status'),
            executor=gettext_lazy('Executor'),
            labels=gettext_lazy('Labels'),
        )
