from task_manager.apps.tools import reverse_lazy, gettext_lazy  # noqa
from .models import Task
from .forms import TaskForm
from .filters import TaskFilterSet
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django_filters.views import FilterView  # noqa
from task_manager.mixins import (
    AuthenticationRequiredMixin,
    SuccessMessageMixin,
    OnlyAuthorCanDeleteTaskMixin,
)
from task_manager.apps.users.models import User


# Create your views here.
class TasksIndexView(AuthenticationRequiredMixin, FilterView):
    template_name = "tasks/index.html"
    model = Task
    filterset_class = TaskFilterSet


class TaskDetailView(AuthenticationRequiredMixin, DetailView):
    template_name = "tasks/details.html"
    model = Task


class TaskCreateView(
    AuthenticationRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    template_name = "tasks/create.html"
    model = Task
    form_class = TaskForm
    success_message = gettext_lazy('Task created successfully')
    success_url = reverse_lazy('tasks_index')

    def form_valid(self, form):
        form.instance.author = User.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)


class TaskUpdateView(
    AuthenticationRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    template_name = "tasks/update.html"
    model = Task
    form_class = TaskForm
    success_message = ('Task updated successfully')
    success_url = reverse_lazy('tasks_index')


class TaskDeleteView(
    AuthenticationRequiredMixin,
    OnlyAuthorCanDeleteTaskMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "tasks/delete.html"
    model = Task
    success_url = reverse_lazy('tasks_index')
    success_message = gettext_lazy('Task deleted successfully')
    not_an_author_url = success_url
    not_an_author_message = gettext_lazy('Only author can delete task')
