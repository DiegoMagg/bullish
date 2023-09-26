from math import ceil

from django.db import models
from django.utils.translation import gettext_lazy as _


class CurrenciModelMixin(models.Model):

    class Currency(models.TextChoices):
        BRL = 'BRL', 'BRL',
        USD = 'USD', 'USD',

    currency = models.CharField(choices=Currency.choices, max_length=3)

    class Meta:
        abstract = True


class Share(CurrenciModelMixin, models.Model):

    class Type(models.TextChoices):
        SHOPPINGS = 'SHOPPINGS', _('Shoppings'),
        CORPORATE_SLABS = 'CORPORATE_SLABS', _('Corporate Slabs'),
        LOGISTICS_SHEDS = 'LOGISTICS_SHEDS', _('Logistics Sheds'),
        HOTELS = 'HOTELS', _('Hotels'),
        EDUCATIONAL = 'EDUCATIONAL', _('Educational'),
        HOSPITAL = 'HOSPITAL', _('Hospital'),
        BANCARY = 'BANCARY', _('Bancary'),
        FUNDS = 'FUNDS', _('Funds'),
        PROPERTY_DEVELOPMENT = 'PROPERTY_DEVELOPMENT', _('Property Development'),
        REAL_ESTATE_RECEIVABLES_CRIS = 'REAL_ESTATE_RECEIVABLES', _('Real Estate Receivables (CRIs)'),
        HYBRID = 'HYBRID', _('Hybrid'),
        AGRO = 'AGRO', _('Agro')

    ticker = models.CharField(max_length=6, unique=True)
    name = models.CharField(unique=True, max_length=255)
    type = models.CharField(max_length=30, choices=Type.choices)
    heritage = models.DecimalField(max_digits=18, decimal_places=2)
    market_value = models.DecimalField(max_digits=18, decimal_places=2)
    reservation = models.DecimalField(max_digits=18, decimal_places=2)
    shareholders_amount = models.PositiveIntegerField()
    quota_amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def p_over_vp(self):
        data = [self.heritage, self.market_value]
        data.sort(reverse=True)
        return data[0] / data[1]

    @property
    def reservation_percentage(self):
        data = [self.heritage, self.reservation]
        data.sort()
        return (data[0] / data[1]) * 100

    @property
    def magic_number(self):
        try:
            last_share_price = self.shareprice_set.latest('created_at').price
            last_dividend_amount = self.dividend_set.filter(paid=True).latest('payment_date').amount
            return ceil(last_share_price / last_dividend_amount)
        except (Dividend.DoesNotExist, SharePrice.DoesNotExist):
            return 0

    def __str__(self):
        return self.ticker

    class Meta:
        db_table = 'shares'
        ordering = ['ticker']


class Dividend(CurrenciModelMixin, models.Model):
    share = models.ForeignKey(Share, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    com_data = models.DateField()
    payment_date = models.DateField(null=True)
    paid = models.BooleanField()

    class Meta:
        db_table = 'dividend'
        ordering = ['share', '-payment_date']


class SharePrice(models.Model):
    share = models.ForeignKey(Share, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=18, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'share_price'
        ordering = ['share', '-created_at']


class FavoriteShare(models.Model):
    share = models.ForeignKey(Share, on_delete=models.PROTECT)
    user = models.ForeignKey('accounts.user', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'favorite_share'
        ordering = ['share']
        unique_together = ['user', 'share']
