from django.urls import path, include
from .views import FollowerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Followers', FollowerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
