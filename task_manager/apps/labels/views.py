from task_manager.tools import reverse_lazy, gettext_lazy  # noqa
from django.views.generic import ListView, CreateView, UpdateView, DeleteView  # noqa
from task_manager.mixins import (
    AuthenticationRequiredMixin,
    SuccessMessageMixin,
    DeleteProtectionMixin,
)
from .models import Label
from .forms import LabelForm


labels_url = reverse_lazy('labels_index')


class LabelsIndexView(AuthenticationRequiredMixin, ListView):
    template_name = 'labels/index.html'
    model = Label


class LabelCreateView(
    AuthenticationRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    template_name = 'labels/create.html'
    model = Label
    form_class = LabelForm
    success_message = gettext_lazy('Label created successfully')
    success_url = labels_url


class LabelUpdateView(
    AuthenticationRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    template_name = 'labels/update.html'
    model = Label
    form_class = LabelForm
    success_message = gettext_lazy('Label updated successfully')
    success_url = labels_url


class LabelDeleteView(
    AuthenticationRequiredMixin,
    DeleteProtectionMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = 'labels/delete.html'
    model = Label
    success_message = gettext_lazy('Label deleted successfully')
    success_url = labels_url
    delete_protection_message = gettext_lazy(
        'Unable to delete. Label is busy.',
    )
    delete_protection_url = labels_url
