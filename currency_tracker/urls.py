from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('currency-data/', views.currency_data, name='currency_data'),
    path('update-currency-rates/', views.update_currency_rates, name='update_currency_rates'),
]
