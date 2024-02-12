from django.urls import path
from .views import (
    UsersIndexView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
)


urlpatterns = [
    path('', UsersIndexView.as_view(), name='users_index'),
    path('create/', UserCreateView.as_view(), name='create_user'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update_user'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete_user'),
]
