from django.shortcuts import render

def index(request):
    return render(request, 'currency_tracker/index.html')
