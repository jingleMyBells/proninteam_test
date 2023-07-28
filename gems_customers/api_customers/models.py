from django.db import models


class Customer(models.Model):

    username = models.CharField(
        'имя покупателя',
        max_length=20,
        unique=True,
    )

    spent_money = models.IntegerField('сумма трат', default=0)

    class Meta:
        ordering = ['-spent_money']
        verbose_name = 'покупатель'
        verbose_name_plural = 'покупатели'

    def __str__(self):
        return self.username


class Item(models.Model):

    title = models.CharField('наименование', max_length=20, unique=True)

    class Meta:
        verbose_name = 'камень'
        verbose_name_plural = 'камни'


class Deal(models.Model):

    money_total = models.IntegerField('сумма сделки')

    quantity = models.IntegerField('количество камней')

    perform_date = models.DateTimeField('дата сделки')

    customer = models.ForeignKey(
        Customer,
        verbose_name='покупатель',
        on_delete=models.SET(None),
        null=True,
        related_name='deals'
    )

    item = models.ForeignKey(
        Item,
        verbose_name='камень',
        on_delete=models.SET(None),
        null=True,
    )
