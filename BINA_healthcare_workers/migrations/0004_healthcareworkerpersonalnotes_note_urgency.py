# Generated by Django 5.0.3 on 2024-03-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BINA_healthcare_workers', '0003_alter_healthcareworkerpersonalnotes_note_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcareworkerpersonalnotes',
            name='note_urgency',
            field=models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], default='LOW', max_length=12),
        ),
    ]
