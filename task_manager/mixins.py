from task_manager.tools import (
    gettext_lazy,
    messages,
    redirect,
    reverse_lazy,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin  # noqa , just for outer imports
from django.db.models import ProtectedError


class AuthenticationRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, gettext_lazy('Forbidden. Please log in.'))
        return redirect(reverse_lazy('login'))


class PermissionMixin(UserPassesTestMixin):
    permission_denied_message = ''
    permission_denied_url = '/'

    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect(self.permission_denied_url)


class DeleteProtectionMixin:
    delete_protection_message = ''
    delete_protection_url = '/'

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.delete_protection_message)
            return redirect(self.delete_protection_url)


class OnlyAuthorCanDeleteTaskMixin(UserPassesTestMixin):
    not_an_author_message = ''
    not_an_author_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().author

    def handle_no_permission(self):
        messages.error(self.request, self.not_an_author_message)
        return redirect(self.not_an_author_url)
