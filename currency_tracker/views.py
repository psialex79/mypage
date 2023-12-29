from django.shortcuts import render
from django.http import JsonResponse
from .models import CurrencyRate, CurrencyPurchase
from .currency_updater import fetch_historical_data
import json

def get_currency_data():
    rates = CurrencyRate.objects.all().order_by('date')
    data_labels = [rate.date.strftime("%Y-%m-%d") for rate in rates]
    data_rates = [str(rate.rate) for rate in rates]
    return data_labels, data_rates

def get_current_rate():
    latest_rate = CurrencyRate.objects.order_by('-date').first()
    return latest_rate.rate if latest_rate else None

def index(request):
    current_rate = get_current_rate()
    purchases = CurrencyPurchase.objects.all().order_by('-date')
    
    for purchase in purchases:
        purchase.current_value = purchase.current_value(current_rate)
        purchase.difference = purchase.difference(current_rate)
        
    data_labels, data_rates = get_currency_data()
    latest_rate = data_rates[-1] if data_rates else 'Нет данных'
    latest_date = data_labels[-1] if data_labels else 'Нет данных'
    purchases = get_currency_purchases()
    context = {
        'data_labels': json.dumps(data_labels),
        'data_rates': json.dumps(data_rates),
        'latest_rate': latest_rate,
        'latest_date': latest_date,
        'purchases': purchases
    }
    return render(request, 'currency_tracker/index.html', context)

def currency_data(request):
    data_labels, data_rates = get_currency_data()
    return JsonResponse({
        'data_labels': data_labels,
        'data_rates': data_rates
    })

def update_currency_rates(request):
    fetch_historical_data()
    return render(request, 'currency_tracker/index.html')

def get_currency_purchases():
    return CurrencyPurchase.objects.all().order_by('-date')