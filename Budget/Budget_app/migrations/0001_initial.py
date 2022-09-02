# Generated by Django 4.1 on 2022-08-05 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
                ('transaction_type', models.BooleanField(default=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Categorie list',
                'verbose_name_plural': 'Categories list',
            },
        ),
        migrations.CreateModel(
            name='CountsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_name', models.CharField(max_length=255)),
                ('balance', models.FloatField(blank=True, null=True)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('card_number', models.CharField(max_length=255)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Count list',
                'verbose_name_plural': 'Counts list',
            },
        ),
        migrations.CreateModel(
            name='CurrencyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_name', models.CharField(max_length=255)),
                ('currency_value', models.FloatField()),
                ('update_dt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Currency list',
                'verbose_name_plural': 'Currencys list',
            },
        ),
        migrations.CreateModel(
            name='CountValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.BooleanField(default=True)),
                ('transaction_value', models.FloatField()),
                ('remainder', models.FloatField()),
                ('description', models.CharField(max_length=255)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Budget_app.categorieslist')),
                ('count_list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Budget_app.countslist')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Budget_app.currencylist')),
            ],
            options={
                'verbose_name': 'Count values',
                'verbose_name_plural': 'Count values',
            },
        ),
    ]