from task_manager.apps.tools import gettext_lazy
from django_filters import FilterSet, BooleanFilter, ModelChoiceFilter
from django.forms import CheckboxInput
from task_manager.apps.statuses.models import Status
from task_manager.apps.users.models import User
from task_manager.apps.labels.models import Label
from task_manager.apps.tasks.models import Task


class TaskFilterSet(FilterSet):
    status = ModelChoiceFilter(
        queryset=Status.objects.all(),
        required=False,
        label=gettext_lazy('Status'),
    )
    executor = ModelChoiceFilter(
        queryset=User.objects.all(),
        required=False,
        label=gettext_lazy('Executor'),
    )
    label = ModelChoiceFilter(
        queryset=Label.objects.all(),
        required=False,
        label=gettext_lazy('Label'),
    )
    own_tasks = BooleanFilter(
        label=gettext_lazy('Own tasks only'),
        widget=CheckboxInput,
        method='get_user_tasks',
    )

    def get_user_tasks(self, tasks, key, value):
        return tasks.filter(author=self.request.user) if value else tasks

    class Meta:
        model = Task
        fields = []
