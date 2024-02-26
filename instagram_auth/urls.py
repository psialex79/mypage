from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.instagram_login, name='instagram_login'),
    path('callback/', views.instagram_callback, name='instagram_callback'),
]