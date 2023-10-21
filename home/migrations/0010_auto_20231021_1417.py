# Generated by Django 3.2 on 2023-10-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_bookingpoda_eta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingpoda',
            old_name='podA',
            new_name='pod_name',
        ),
        migrations.RenameField(
            model_name='bookingpoda',
            old_name='podA_rate',
            new_name='pod_rate',
        ),
        migrations.RenameField(
            model_name='bookingpodb',
            old_name='podB',
            new_name='pod_name',
        ),
        migrations.RenameField(
            model_name='bookingpodb',
            old_name='podB_rate',
            new_name='pod_rate',
        ),
        migrations.AddField(
            model_name='bookingpodb',
            name='eta',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
