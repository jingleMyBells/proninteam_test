# Generated by Django 4.2.3 on 2023-07-27 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('spent_money', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money_total', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('perform_date', models.DateTimeField()),
                ('customer', models.ForeignKey(null=True, on_delete=models.SET(None), to='api_customers.customer')),
                ('item', models.ForeignKey(null=True, on_delete=models.SET(None), to='api_customers.item')),
            ],
        ),
    ]