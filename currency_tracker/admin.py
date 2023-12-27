from django.contrib import admin
from .models import CurrencyRate, CurrencyPurchase

@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ('date', 'rate')

@admin.register(CurrencyPurchase)
class CurrencyPurchaseAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'rate')