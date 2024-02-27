import requests, time, logging
from datetime import date, timedelta
from .models import CurrencyRate, BitcoinRate
from django.core.exceptions import ObjectDoesNotExist

# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_historical_data():
    start_date = date(2023, 1, 1)
    end_date = date.today()
    delta = timedelta(days=1)
    api_key = '714baec2f2d29eb8f76c12cff4dbcf45'

    while start_date <= end_date:
        try:
            CurrencyRate.objects.get(date=start_date)
            logger.info(f'Данные за {start_date} уже есть в базе данных.')
        except ObjectDoesNotExist:
            formatted_date = start_date.strftime('%Y-%m-%d')
            url = f'http://api.exchangeratesapi.io/v1/{formatted_date}?access_key={api_key}&symbols=RUB,USD'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if 'rates' in data and 'RUB' in data['rates'] and 'USD' in data['rates']:
                    eur_to_rub = data['rates']['RUB']
                    eur_to_usd = data['rates']['USD']
                    usd_to_rub = eur_to_rub / eur_to_usd
                    rate = CurrencyRate(date=start_date, rate=usd_to_rub)
                    rate.save()
                    logger.info(f'Курс USD/RUB за {formatted_date} добавлен в базу данных.')
                else:
                    logger.warning(f'Нет данных о курсе валют для {formatted_date}')
            else:
                logger.error(f'Ошибка запроса к API для {formatted_date}: {response.status_code}')
        start_date += delta

def fetch_historical_btc_usd_data():
    start_date = date(2023, 1, 1)
    end_date = date.today()
    delta = timedelta(days=1)

    while start_date <= end_date:
        try:
            BitcoinRate.objects.get(date=start_date)
            logger.info(f'Данные по BTC/USD за {start_date} уже есть в базе данных.')
        except ObjectDoesNotExist:
            time.sleep(1.2)  # Соблюдайте ограничения API
            formatted_date = start_date.strftime('%d-%m-%Y')
            url = f'https://api.coingecko.com/api/v3/coins/bitcoin/history?date={formatted_date}&localization=false'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if 'market_data' in data and 'current_price' in data['market_data'] and 'usd' in data['market_data']['current_price']:
                    btc_to_usd = data['market_data']['current_price']['usd']
                    rate = BitcoinRate(date=start_date, rate=btc_to_usd)
                    rate.save()
                    logger.info(f'Курс BTC/USD за {formatted_date} добавлен в базу данных.')
                else:
                    logger.warning(f'Нет данных о курсе BTC-USD для {formatted_date}')
            else:
                logger.error(f'Ошибка запроса к API для {formatted_date}: {response.status_code}')
        start_date += delta
