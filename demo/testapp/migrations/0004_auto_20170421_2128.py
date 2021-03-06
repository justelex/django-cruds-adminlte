# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import testapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_addresses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered', models.BooleanField(help_text='Registered yet?', verbose_name='Registered')),
                ('sent', models.BooleanField(help_text='Invoice sent?', verbose_name='Sent')),
                ('paid', models.BooleanField(help_text='Invoice paid?', verbose_name='Paid')),
                ('date', models.DateTimeField(verbose_name='Creation date')),
                ('invoice_number', models.CharField(default=testapp.models.last_number, max_length=50, verbose_name='Invoice Number')),
                ('description1', models.TextField(blank=True, verbose_name='Description header')),
                ('description2', models.TextField(blank=True, verbose_name='Description footer')),
                ('subtotal', models.CharField(blank=True, help_text='Calculated field', max_length=200, verbose_name='Subtotal')),
                ('subtotal_iva', models.CharField(blank=True, help_text='Calculated field', max_length=200, verbose_name='Subtotal IVA')),
                ('subtotal_retentions', models.CharField(blank=True, help_text='Calculated field', max_length=200, verbose_name='Subtotal Retentions')),
                ('total', models.CharField(blank=True, help_text='Calculated field', max_length=200, verbose_name='Total')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='testapp.Customer')),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
            },
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=200, verbose_name='Reference')),
                ('concept', models.CharField(max_length=200, verbose_name='Concept')),
                ('quantity', models.CharField(max_length=200, verbose_name='Quantity')),
                ('unit', models.CharField(help_text='(days, hours...)', max_length=200, verbose_name='Unit')),
                ('unit_price', models.CharField(max_length=200, verbose_name='Unit Price')),
                ('amount', models.CharField(max_length=200, verbose_name='Ammount')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line', to='testapp.Invoice')),
            ],
            options={
                'verbose_name': 'Line',
                'verbose_name_plural': 'Lines',
            },
        ),
        migrations.AddField(
            model_name='addresses',
            name='status',
            field=models.BooleanField(default=True, help_text='Active?', verbose_name='Status'),
        ),
    ]
