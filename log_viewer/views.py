from django.shortcuts import render
from django.http import HttpResponse
import os

def log_viewer(request):
    with open('/var/log/eduhelperbot.err.log', 'r') as file:
        logs = file.read()
    return render(request, 'log_viewer.html', {'logs': logs})
