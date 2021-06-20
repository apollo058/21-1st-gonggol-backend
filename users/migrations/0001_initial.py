# Generated by Django 3.2.3 on 2021-06-18 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=45)),
                ('postal', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=50)),
                ('address_detail', models.CharField(max_length=45)),
                ('phone_number', models.CharField(max_length=13)),
                ('sms_reception', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=45, unique=True)),
                ('email_reception', models.BooleanField(default=False)),
                ('product', models.ManyToManyField(through='products.Like', to='products.Product')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
