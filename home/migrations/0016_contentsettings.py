# Generated by Django 3.2 on 2023-12-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_bookingpodb_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_name', models.CharField(blank=True, max_length=200, null=True)),
                ('content', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]