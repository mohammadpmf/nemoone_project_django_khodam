# Generated by Django 4.2.6 on 2024-02-18 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0002_alter_estate_area_alter_estate_street_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='floor',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='طبقه'),
        ),
    ]