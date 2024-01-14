from django.urls import path
from . import views

urlpatterns = [
    path('log-viewer', views.log_viewer, name='log_viewer'),
]
