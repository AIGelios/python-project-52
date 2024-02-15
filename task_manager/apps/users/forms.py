from task_manager.tools import gettext_lazy
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField
from .models import User


class UserForm(UserCreationForm):
    first_name = CharField(
        max_length=150,
        required=1,
        label=gettext_lazy('First name'),
    )
    last_name = CharField(
        max_length=150,
        required=1,
        label=gettext_lazy('Last name'),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        )

    def clean_username(self):
        return self.cleaned_data.get('username')
