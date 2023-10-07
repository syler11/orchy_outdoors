# Generated by Django 3.2 on 2023-10-07 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PodAAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('rate', models.CharField(default='80', max_length=10)),
                ('status', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PodBAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('rate', models.CharField(default='80', max_length=10)),
                ('status', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]