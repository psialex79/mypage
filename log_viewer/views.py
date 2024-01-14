from django.shortcuts import render
import re

def filter_and_trim_logs(logs):
    # Регулярное выражение для поиска русского текста
    russian_text_re = re.compile(r'[А-Яа-я]+.*')

    filtered_logs = []
    for log in logs:
        # Ищем совпадение с русским текстом
        match = russian_text_re.search(log)
        if match:
            # Добавляем обрезанную строку (только русский текст и все, что после)
            filtered_logs.append(match.group())

    return filtered_logs

# Использование функции в вашем представлении
def log_viewer(request):
    with open('/var/log/eduhelperbot.err.log', 'r') as file:
        logs = file.readlines() # читаем логи построчно

    logs.reverse() # переворачиваем список, чтобы новые сообщения были в начале
    filtered_logs = filter_and_trim_logs(logs) # фильтруем и обрезаем логи
    return render(request, 'log_viewer/log_viewer.html', {'logs': filtered_logs})
