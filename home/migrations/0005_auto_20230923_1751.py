# Generated by Django 3.2 on 2023-09-23 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20230923_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingpoda',
            old_name='podA_pax',
            new_name='pax',
        ),
        migrations.RenameField(
            model_name='bookingpodb',
            old_name='podB_pax',
            new_name='pax',
        ),
        migrations.AlterField(
            model_name='bookingpoda',
            name='notes',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]