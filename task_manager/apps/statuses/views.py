from task_manager.apps.tools import reverse_lazy, gettext_lazy  # noqa
from django.views.generic import ListView, CreateView, UpdateView, DeleteView  # noqa
from task_manager.mixins import (
    AuthenticationRequiredMixin,
    SuccessMessageMixin,
    DeleteProtectionMixin,
)
from .models import Status
from .forms import StatusForm


statuses_url = reverse_lazy('statuses_index')


class StatusesIndexView(AuthenticationRequiredMixin, ListView):
    template_name = 'statuses/index.html'
    model = Status


class StatusCreateView(
    AuthenticationRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    template_name = 'statuses/create.html'
    model = Status
    form_class = StatusForm
    success_message = gettext_lazy('Status created successfully')
    success_url = statuses_url


class StatusUpdateView(
    AuthenticationRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    template_name = 'statuses/update.html'
    model = Status
    form_class = StatusForm
    success_message = gettext_lazy('Status updated successfully')
    success_url = statuses_url


class StatusDeleteView(
    AuthenticationRequiredMixin,
    DeleteProtectionMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = 'statuses/delete.html'
    model = Status
    success_message = gettext_lazy('Status deleted successfully')
    success_url = statuses_url
    delete_protection_message = gettext_lazy(
        'Unable to delete. Status is busy.',
    )
    delete_protection_url = statuses_url
