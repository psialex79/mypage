from django.shortcuts import render
from django.http import HttpResponse
import os
import re


def log_viewer(request):
    with open('/var/log/eduhelperbot.err.log', 'r') as file:
        logs = file.readlines() # читаем логи построчно

    logs.reverse() # переворачиваем список, чтобы новые сообщения были в начале
    return render(request, 'log_viewer/log_viewer.html', {'logs': logs})

