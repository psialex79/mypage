from rest_framework import viewsets
from .models import Follower
from .serializers import FollowerSerializer
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from .forms import FollowerForm

class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

@require_POST
def add_follower(request):
    form = FollowerForm(request.POST)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect('/users-checker/')

def list_followers(request):
    followers = Follower.objects.all()
    return render(request, 'users_checker/user_manager.html', {'followers': followers})
