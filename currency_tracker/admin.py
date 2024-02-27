from django.contrib import admin
from .models import CurrencyRate, CurrencyPurchase, BitcoinRate, BitcoinPurchase

@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ('date', 'rate')
    list_filter = ('date',)
    search_fields = ('date', 'rate')

@admin.register(CurrencyPurchase)
class CurrencyPurchaseAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'rate', 'spent_amount')
    list_filter = ('date',)
    search_fields = ('date', 'amount')

@admin.register(BitcoinRate)
class BitcoinRateAdmin(admin.ModelAdmin):
    list_display = ('date', 'rate')
    list_filter = ('date',)
    search_fields = ('date', 'rate')

@admin.register(BitcoinPurchase)
class BitcoinPurchaseAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'rate', 'spent_amount_usd')
    list_filter = ('date',)
    search_fields = ('date', 'amount')

