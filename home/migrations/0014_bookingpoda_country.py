# Generated by Django 3.2 on 2023-11-23 19:41

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20231114_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingpoda',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
