# Generated by Django 4.2.11 on 2024-05-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тітул')),
                ('description', models.TextField(verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Информація про нас',
                'verbose_name_plural': 'Информація про нас',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер телефону')),
                ('email', models.EmailField(max_length=254, verbose_name='Emeil')),
            ],
            options={
                'verbose_name': 'Шапка сайта',
                'verbose_name_plural': 'Шапка сайта',
            },
        ),
        migrations.CreateModel(
            name='PaymentDelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тітул')),
                ('description', models.TextField(verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Оплата та доставка',
                'verbose_name_plural': 'Оплата та доставка',
            },
        ),
        migrations.CreateModel(
            name='ReturnAgoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тітул')),
                ('description', models.TextField(verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Повернення товару',
                'verbose_name_plural': 'Повернення товару',
            },
        ),
        migrations.CreateModel(
            name='Safeguards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тітул')),
                ('description', models.TextField(verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Гарантії',
                'verbose_name_plural': 'Гарантії',
            },
        ),
    ]
