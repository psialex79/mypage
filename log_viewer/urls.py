from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_viewer, name='log_viewer'),
]

