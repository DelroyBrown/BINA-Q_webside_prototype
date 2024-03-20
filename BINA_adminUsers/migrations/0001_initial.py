# Generated by Django 5.0.3 on 2024-03-20 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BINA_departments', '0001_initial'),
        ('BINA_organisations', '0001_initial'),
        ('BINA_roles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('other_names', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('personal_ods_code', models.CharField(default='A12345', max_length=10)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BINA_departments.department')),
                ('organisation_you_work_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BINA_organisations.organisation')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BINA_roles.role')),
            ],
        ),
    ]
