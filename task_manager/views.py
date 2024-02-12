from task_manager.apps.tools import gettext_lazy, reverse_lazy, messages
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from .mixins import SuccessMessageMixin


class HomePageView(TemplateView):
    template_name = 'index.html'


class TaskManLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_message = gettext_lazy('Logged in successfully')
    next_page = reverse_lazy('homepage')


class TaskManLogoutView(SuccessMessageMixin, LogoutView):
    success_message = gettext_lazy('Logged out successfully')
    next_page = reverse_lazy('homepage')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, self.success_message)
        return super().dispatch(request, *args, **kwargs)
