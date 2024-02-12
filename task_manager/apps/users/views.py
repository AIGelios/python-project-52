from task_manager.apps.tools import gettext_lazy, reverse_lazy
from .models import User
from .forms import UserForm
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from task_manager.mixins import (
    AuthenticationRequiredMixin,
    PermissionMixin,
    SuccessMessageMixin,
    DeleteProtectionMixin,
)


class UsersIndexView(ListView):
    template_name = 'users/index.html'
    model = User


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = gettext_lazy('Registration successful')


class UserUpdateView(
    AuthenticationRequiredMixin,
    PermissionMixin,
    SuccessMessageMixin,
    UpdateView
):
    template_name = 'users/update.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users_index')
    success_message = gettext_lazy('User updation successful')
    permission_denied_url = success_url
    permission_denied_message = gettext_lazy('User only can update himself')


class UserDeleteView(
    AuthenticationRequiredMixin,
    PermissionMixin,
    DeleteProtectionMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('users_index')
    success_message = gettext_lazy('User deletion successful')
    permission_denied_url = success_url
    permission_denied_message = gettext_lazy('User only can update himself')
    delete_protection_url = success_url
    delete_protection_message = gettext_lazy('Unable to delete. User is busy.')
