# Generated by Django 4.2.6 on 2024-02-18 17:04

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0004_estate_postal_code_alter_estate_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='year_created',
            field=django_jalali.db.models.jDateField(default=1402, verbose_name='سال ساخت'),
        ),
    ]
