from django.db import models


class Customer(models.Model):

    username = models.CharField(max_length=20, unique=True)

    spent_money = models.IntegerField(default=0)

    class Meta:
        ordering = ['-spent_money']


class Item(models.Model):

    title = models.CharField(max_length=20, unique=True)


class Deal(models.Model):

    money_total = models.IntegerField()

    quantity = models.IntegerField()

    perform_date = models.DateTimeField()

    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET(None),
        null=True,
        related_name='deals'
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.SET(None),
        null=True,
    )

