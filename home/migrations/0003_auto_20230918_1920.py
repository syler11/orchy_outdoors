# Generated by Django 3.2 on 2023-09-18 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20230916_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingPodA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(blank=True, max_length=10, null=True)),
                ('podA', models.CharField(blank=True, max_length=20, null=True)),
                ('podA_pax', models.IntegerField(blank=True, null=True)),
                ('nights', models.IntegerField(blank=True, null=True)),
                ('arrival_date', models.DateField(null=True)),
                ('podA_rate', models.IntegerField(blank=True, null=True)),
                ('total_cost', models.IntegerField(blank=True, null=True)),
                ('fname', models.CharField(blank=True, max_length=150, null=True)),
                ('lname', models.CharField(blank=True, max_length=150, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('notes', models.CharField(blank=True, max_length=150, null=True)),
                ('status', models.CharField(blank=True, default='Available', max_length=150, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookingPodB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(blank=True, max_length=10, null=True)),
                ('podB', models.CharField(blank=True, max_length=20, null=True)),
                ('podB_pax', models.IntegerField(blank=True, null=True)),
                ('nights', models.IntegerField(blank=True, null=True)),
                ('arrival_date', models.DateField(null=True)),
                ('podB_rate', models.IntegerField(blank=True, null=True)),
                ('total_cost', models.IntegerField(blank=True, null=True)),
                ('fname', models.CharField(blank=True, max_length=150, null=True)),
                ('lname', models.CharField(blank=True, max_length=150, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('notes', models.CharField(blank=True, max_length=150, null=True)),
                ('status', models.CharField(blank=True, default='Available', max_length=150, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]