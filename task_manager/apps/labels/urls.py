from django.urls import path
from .views import (
    LabelsIndexView,
    LabelCreateView,
    LabelUpdateView,
    LabelDeleteView,
)


urlpatterns = [
    path('', LabelsIndexView.as_view(), name='labels_index'),
    path('create/', LabelCreateView.as_view(), name='create_label'),
    path('<int:pk>/update/', LabelUpdateView.as_view(), name='update_label'),
    path('<int:pk>/delete/', LabelDeleteView.as_view(), name='delete_label'),
]
