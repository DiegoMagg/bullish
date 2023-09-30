from django.contrib import admin
from shares import models


@admin.register(models.Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = [
        'ticker',
        'name',
        'type',
        'p_over_vp',
        'magic_number',
        'reservation_percentage',
        'heritage',
        'market_value',
        'reservation',
        'shareholders_amount',
        'quota_amount',
        'created_at',
        'updated_at',
    ]


@admin.register(models.Dividend)
class DividendAdmin(admin.ModelAdmin):
    list_display = [
        'share',
        'amount',
        'com_data',
        'payment_date',
        'paid',
    ]


@admin.register(models.SharePrice)
class SharePriceAdmin(admin.ModelAdmin):
    list_display = ['share', 'price', 'created_at']


@admin.register(models.FavoriteShare)
class FavoriteShareAdmin(admin.ModelAdmin):
    pass
