from django.core.management.base import BaseCommand
import requests
from datetime import date, timedelta
from currency_tracker.models import CurrencyRate

class Command(BaseCommand):
    help = 'Fetches historical currency rates'

    def handle(self, *args, **options):
        start_date = date(2023, 1, 1)
        end_date = date.today()
        api_key = 'd23e4cbf56f3359cbfc6bdfa09a99ad1'

        while start_date <= end_date:
            if not CurrencyRate.objects.filter(date=start_date).exists():
                formatted_date = start_date.strftime('%Y-%m-%d')
                url = f'http://api.exchangeratesapi.io/v1/{formatted_date}?access_key={api_key}&symbols=RUB'
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    if 'rates' in data and 'RUB' in data['rates']:
                        rate = CurrencyRate(date=start_date, rate=data['rates']['RUB'])
                        rate.save()
                    else:
                        print(f'Нет данных о курсе валют для {formatted_date}')
                else:
                    print(f'Ошибка запроса к API для {formatted_date}: {response.status_code}')
            else:
                print(f'Данные за {start_date} уже есть в базе данных.')
            start_date += timedelta(days=1)
