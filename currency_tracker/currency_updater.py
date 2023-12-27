import requests
from datetime import date, timedelta
from .models import CurrencyRate
from django.core.exceptions import ObjectDoesNotExist

def fetch_historical_data():
    start_date = date(2023, 1, 1)
    end_date = date.today()
    delta = timedelta(days=1)
    api_key = '714baec2f2d29eb8f76c12cff4dbcf45'

    while start_date <= end_date:
        try:
            CurrencyRate.objects.get(date=start_date)
            print(f'Данные за {start_date} уже есть в базе данных.')
        except ObjectDoesNotExist:
            formatted_date = start_date.strftime('%Y-%m-%d')
            url = f'http://api.exchangeratesapi.io/v1/{formatted_date}?access_key={api_key}&base=USD&symbols=RUB'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if 'rates' in data and 'RUB' in data['rates']:
                    rate = CurrencyRate(date=start_date, rate=data['rates']['RUB'])
                    rate.save()
                    print(f'Данные за {formatted_date} добавлены в базу данных.')
                else:
                    print(f'Нет данных о курсе валют для {formatted_date}')
            else:
                print(f'Ошибка запроса к API для {formatted_date}: {response.status_code}')
        start_date += delta
