from django.contrib.auth.models import User
from django.db import models


def get_first_name(self):
    return f'{self.first_name} {self.last_name}'


User.add_to_class("__str__", get_first_name)


class CountsList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    count_name = models.CharField(max_length=255)
    balance = models.FloatField(null=True, blank=True)
    create_dt = models.DateTimeField(auto_now_add=True)
    card_token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.user_id.first_name} {self.user_id.last_name} {self.count_name}'

    class Meta:
        verbose_name = 'Count list'
        verbose_name_plural = 'Counts list'


class CategoriesList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=255)
    transaction_type = models.BooleanField(default=True)

    def __str__(self):
        if self.transaction_type == 1:
            return f'{self.user_id.first_name} {self.user_id.last_name} "{self.category_name}" Доходы'
        return f'{self.user_id.first_name} {self.user_id.last_name} "{self.category_name}" Расходы'

    class Meta:
        verbose_name = 'Categorie list'
        verbose_name_plural = 'Categories list'


class CountValues(models.Model):
    count_list_id = models.ForeignKey('CountsList', on_delete=models.CASCADE)
    transaction_type = models.BooleanField(default=True)
    transaction_value = models.FloatField()
    remainder = models.FloatField()
    description = models.CharField(max_length=255)
    category = models.ForeignKey('CategoriesList', on_delete=models.CASCADE)
    currency = models.ForeignKey('CurrencyList', on_delete=models.CASCADE)
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.transaction_type:
            return f'{self.category.category_name} +{self.transaction_value}{self.currency.currency_name}'
        return f'{self.category.category_name} -{self.transaction_value}{self.currency.currency_name}'

    class Meta:
        verbose_name = 'Count values'
        verbose_name_plural = 'Count values'


class CurrencyList(models.Model):
    currency_name = models.CharField(max_length=255)
    currency_value = models.FloatField()
    update_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.currency_name

    class Meta:
        verbose_name = 'Currency list'
        verbose_name_plural = 'Currencys list'
