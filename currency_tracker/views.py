from django.shortcuts import render
from django.http import JsonResponse
from .models import CurrencyRate
import json

def get_currency_data():
    rates = CurrencyRate.objects.all().order_by('date')
    data_labels = [rate.date.strftime("%Y-%m-%d") for rate in rates]
    data_rates = [rate.rate for rate in rates]
    return data_labels, data_rates

def index(request):
    data_labels, data_rates = get_currency_data()
    context = {
        'data_labels': json.dumps(data_labels),
        'data_rates': json.dumps(data_rates)
    }
    return render(request, 'currency_tracker/index.html', context)

def currency_data(request):
    data_labels, data_rates = get_currency_data()
    return JsonResponse({
        'data_labels': data_labels,
        'data_rates': data_rates
    })
