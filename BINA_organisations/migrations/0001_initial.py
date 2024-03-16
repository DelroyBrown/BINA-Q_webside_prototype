# Generated by Django 5.0.3 on 2024-03-14 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_name', models.CharField(default='', max_length=100)),
                ('building_name_or_number', models.CharField(default='', max_length=100)),
                ('street', models.CharField(default='', max_length=100)),
                ('town_or_city', models.CharField(default='', max_length=100)),
                ('county', models.CharField(default='', max_length=100)),
                ('postcode', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('ods_code', models.CharField(default='', max_length=25)),
            ],
        ),
    ]