from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('currency-data/', views.currency_data, name='currency_data'),
    path('update-currency-rates/', views.update_currency_rates, name='update_currency_rates'),
    path('log-viewer/', include('log_viewer.urls')),
]
