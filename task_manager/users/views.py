from .models import User

from django.views.generic import (
    ListView,
    CreateView,
)

from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserForm

from django.utils.translation import gettext_lazy


class UsersIndexView(ListView):
    template_name = 'users/index.html'
    model = User


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    model = User
    form_class = UserForm
    success_url = '/'
    success_message = gettext_lazy('Registration successful')
