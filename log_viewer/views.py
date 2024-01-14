from django.shortcuts import render
from django.http import HttpResponse
import os
import re

def filter_russian_text(logs):
    # Регулярное выражение для поиска русскоязычных фрагментов
    russian_text_pattern = re.compile(r'[А-Яа-яЁё]+[\w\s]*[А-Яа-яЁё]+')

    filtered_logs = []
    for line in logs:
        # Извлекаем русскоязычные фрагменты из строки
        russian_texts = russian_text_pattern.findall(line)
        if russian_texts:
            # Соединяем все найденные фрагменты в одну строку
            filtered_line = ' '.join(russian_texts)
            filtered_logs.append(filtered_line)
    
    return filtered_logs

def log_viewer(request):
    with open('/var/log/eduhelperbot.err.log', 'r') as file:
        logs = file.readlines() # читаем логи построчно

    filtered_logs = filter_russian_text(logs) # фильтруем логи
    return render(request, 'log_viewer/log_viewer.html', {'logs': filtered_logs})
