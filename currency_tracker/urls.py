from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('currency-data/', views.currency_data, name='currency_data'),
    path('update-currency-rates/', views.update_currency_rates, name='update_currency_rates'),
    path('bitcoin/', views.bitcoin_index, name='bitcoin_index'),
    path('bitcoin-data/', views.bitcoin_data, name='bitcoin_data'),
    path('update-bitcoin-rates/', views.update_bitcoin_rates, name='update_bitcoin_rates'),
]
