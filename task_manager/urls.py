from django.contrib import admin
from django.urls import path, include
from .views import (
    HomePageView,
    TaskManLoginView,
    TaskManLogoutView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='homepage'),
    path('login/', TaskManLoginView.as_view(), name='login'),
    path('logout/', TaskManLogoutView.as_view(), name='logout'),
    path('users/', include('task_manager.apps.users.urls')),
    path('statuses/', include('task_manager.apps.statuses.urls')),
    path('tasks/', include('task_manager.apps.tasks.urls'))
]
