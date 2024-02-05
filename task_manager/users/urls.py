from django.urls import path
from .views import (
    UsersIndexView,
    UserCreateView,
)


urlpatterns = [
    path('', UsersIndexView.as_view(), name='users_index'),
    path('create/', UserCreateView.as_view(), name='create_user'),
]
