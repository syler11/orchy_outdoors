# Generated by Django 3.2 on 2023-12-14 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_contentsettings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookingpoda',
            options={'verbose_name_plural': 'POD A'},
        ),
        migrations.AlterModelOptions(
            name='bookingpodb',
            options={'verbose_name_plural': 'POD B'},
        ),
        migrations.AlterModelOptions(
            name='contentsettings',
            options={'verbose_name_plural': 'Content'},
        ),
        migrations.AlterModelOptions(
            name='pagesettings',
            options={'verbose_name_plural': 'Page Settings'},
        ),
        migrations.AlterField(
            model_name='contentsettings',
            name='content',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]