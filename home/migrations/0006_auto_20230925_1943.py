# Generated by Django 3.2 on 2023-09-25 19:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20230923_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingpoda',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookingpodb',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]