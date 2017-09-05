# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-05 22:13
from __future__ import unicode_literals

import datetime
from decimal import Decimal
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('time_created', models.DateTimeField(default=datetime.datetime.now)),
                ('time_modified', models.DateTimeField(default=datetime.datetime.now)),
                ('shipping_method', models.IntegerField(choices=[(1, b'USPS'), (2, b'FedEx'), (3, b'UPS'), (4, b'DHL')])),
                ('shipping_detail', models.CharField(blank=True, max_length=100)),
                ('payment_detail', models.CharField(blank=True, max_length=200)),
                ('start_time', models.DateTimeField(help_text='Format (Hour & Minute are optional): 10/25/2006 14:30')),
                ('end_time', models.DateTimeField(help_text='Format (Hour & Minute are optional): 10/25/2006 14:30')),
                ('starting_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5)),
                ('shipping_fee', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5)),
                ('reserve_price', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('time_created', models.DateTimeField(default=datetime.datetime.now)),
                ('time_modified', models.DateTimeField(default=datetime.datetime.now)),
                ('amount', models.DecimalField(decimal_places=2, default=Decimal('0.00'), help_text='All bids are final. Price in US dollars.', max_digits=5)),
                ('auction_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='boxer.AuctionEvent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freighter', models.IntegerField()),
                ('departure', models.CharField(max_length=256)),
                ('arrival', models.CharField(max_length=256)),
                ('deadline', models.DateTimeField(auto_now=True)),
                ('volume', models.FloatField()),
                ('weight', models.FloatField()),
                ('image', models.ImageField(max_length=128, upload_to=b'')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Freighter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=64)),
                ('region', models.CharField(max_length=64)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('time_created', models.DateTimeField(default=datetime.datetime.now)),
                ('time_modified', models.DateTimeField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('condition', models.IntegerField(choices=[(1, b'Used'), (2, b'Used Like New'), (3, b'New')])),
                ('status', models.IntegerField(choices=[(1, b'Idle'), (2, b'Running'), (3, b'On Hold'), (4, b'Sold'), (5, b'Expired'), (6, b'Disputed')], default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('time_created', models.DateTimeField(default=datetime.datetime.now)),
                ('time_modified', models.DateTimeField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boxer.ItemCategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('time_created', models.DateTimeField(default=datetime.datetime.now)),
                ('time_modified', models.DateTimeField(default=datetime.datetime.now)),
                ('payment_status', models.IntegerField(choices=[(1, b'Processing'), (2, b'Cleared'), (3, b'Disputed'), (4, b'Refunded')], default=1)),
                ('invoice_number', models.CharField(max_length=200, unique=True)),
                ('auction_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='boxer.AuctionEvent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('time_created', models.DateTimeField(default=datetime.datetime.now)),
                ('time_modified', models.DateTimeField(default=datetime.datetime.now)),
                ('paypal_email', models.EmailField(max_length=254)),
                ('default_shipping_method', models.IntegerField(choices=[(1, b'USPS'), (2, b'FedEx'), (3, b'UPS'), (4, b'DHL')], default=1)),
                ('default_shipping_detail', models.CharField(blank=True, max_length=100, null=True)),
                ('default_payment_detail', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address_line_1', models.CharField(max_length=100)),
                ('address_line_2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', localflavor.us.models.USStateField(max_length=2)),
                ('zipcode', models.CharField(max_length=10)),
                ('phone', localflavor.us.models.PhoneNumberField(max_length=20)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='seller',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='boxer.User'),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction_items', to='boxer.ItemCategory'),
        ),
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction_items', to='boxer.User'),
        ),
        migrations.AddField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='boxer.User'),
        ),
        migrations.AddField(
            model_name='auctionevent',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction_events', to='boxer.Item'),
        ),
        migrations.AddField(
            model_name='auctionevent',
            name='winning_bidder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='won_auctions', to='boxer.User'),
        ),
    ]
