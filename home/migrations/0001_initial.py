# Generated by Django 3.2 on 2023-09-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=10, null=True)),
                ('pod1', models.CharField(max_length=10, null=True)),
                ('pod2', models.CharField(max_length=10, null=True)),
                ('pod1_pax', models.IntegerField(blank=True, null=True)),
                ('pod2_pax', models.IntegerField(blank=True, null=True)),
                ('nights', models.IntegerField(blank=True, null=True)),
                ('arrival_date', models.DateField(null=True)),
                ('pod1_rate', models.IntegerField(blank=True, null=True)),
                ('pod2_rate', models.IntegerField(blank=True, null=True)),
                ('total_cost', models.IntegerField(null=True)),
                ('fname', models.CharField(max_length=150, null=True)),
                ('lname', models.CharField(max_length=150, null=True)),
                ('phone_number', models.CharField(max_length=150, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('notes', models.CharField(blank=True, max_length=150, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]