from .models import User

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserForm

from django.utils.translation import gettext_lazy
from django.urls import reverse_lazy


class UsersIndexView(ListView):
    template_name = 'users/index.html'
    model = User


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    model = User
    form_class = UserForm
    success_url = '/'
    success_message = gettext_lazy('Registration successful')


class UserUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'users/update.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users_index')
    success_message = gettext_lazy('User updation successful')


class UserDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('users_index')
    success_message = gettext_lazy('User deletion successful')
