from django.shortcuts import render
from .models import CurrencyRate
import json

def index(request):
    rates = CurrencyRate.objects.all().order_by('date')
    data_labels = [rate.date.strftime("%Y-%m-%d") for rate in rates]
    data_rates = [rate.rate for rate in rates]
    context = {
        'data_labels': json.dumps(data_labels),
        'data_rates': json.dumps(data_rates)
    }
    return render(request, 'currency_tracker/index.html', context)
