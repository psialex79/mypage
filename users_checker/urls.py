from django.urls import path, include
from .views import FollowerViewSet, list_followers, add_follower
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'followers', FollowerViewSet)

urlpatterns = [
    path('', list_followers, name='list_followers'),  # URL для списка пользователей
    path('add/', add_follower, name='add_follower'),  # URL для добавления нового пользователя
    path('api/', include(router.urls)),  # URL для API
]
