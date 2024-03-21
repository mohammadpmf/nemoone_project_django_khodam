# Generated by Django 4.2.6 on 2024-02-18 20:07

from django.db import migrations
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0011_alter_estate_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='datetime_created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]