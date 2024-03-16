# Generated by Django 5.0.3 on 2024-03-14 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(default='', max_length=100)),
                ('department_type', models.CharField(choices=[('ADM', 'Administration'), ('CLN', 'Clinical Services'), ('CRD', 'Cardiology'), ('DER', 'Dermatology'), ('END', 'Endocrinology'), ('GAS', 'Gastroenterology'), ('GER', 'Geriatrics'), ('HEM', 'Hematology'), ('INF', 'Infectious Diseases'), ('MEN', 'Mental Health'), ('NEU', 'Neurology'), ('ONC', 'Oncology'), ('PED', 'Pediatrics'), ('PSY', 'Psychiatry'), ('RAD', 'Radiology'), ('SUR', 'Surgery'), ('URO', 'Urology')], default='', max_length=50)),
                ('department_id', models.CharField(default='CRD-001', max_length=20)),
                ('department_contact_number', models.CharField(blank=True, default='07795128311', max_length=100, null=True)),
            ],
        ),
    ]