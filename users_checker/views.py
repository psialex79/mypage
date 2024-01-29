from rest_framework import viewsets
from .models import Follower
from .serializers import FollowerSerializer

class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
