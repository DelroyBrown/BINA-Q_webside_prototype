# Generated by Django 5.0.3 on 2024-03-14 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('AHP', 'Allied Health Professional'), ('HA', 'Healthcare Administrator'), ('HCA', 'Healthcare Assistant'), ('MGT', 'Healthcare Manager'), ('HCW', 'Healthcare Worker'), ('HR', 'Hospital Receptionist'), ('LAC', 'Lactation Consultant'), ('LPN', 'Licensed Practical Nurse'), ('MA', 'Medical Assistant'), ('MAA', 'Medical Administrative Assistant'), ('MOA', 'Medical Office Assistant'), ('MS', 'Medical Secretary'), ('MD', 'Medical Doctor'), ('MT', 'Medical Technologist'), ('MHN', 'Mental Health Nurse'), ('NP', 'Nurse Practitioner'), ('OT', 'Occupational Therapist'), ('PA', 'Physician Assistant'), ('PC', 'Patient Coordinator'), ('PH', 'Pharmacist'), ('PT', 'Physical Therapist'), ('PTA', 'Physical Therapist Assistant'), ('PCN', 'Primary Care Nurse'), ('PSY', 'Psychiatrist'), ('CPS', 'Child Psychologist'), ('CNS', 'Clinical Nurse Specialist'), ('CP', 'Clinical Psychologist'), ('CHN', 'Community Health Nurse'), ('CA', 'Clinic Administrator'), ('CCO', 'Care Coordinator'), ('CNA', 'Certified Nursing Assistant'), ('DT', 'Dietitian'), ('EMS', 'Emergency Medical Technician'), ('GEN', 'Genetic Counselor'), ('HIT', 'Health Information Technician'), ('HSM', 'Health Services Manager'), ('PSYT', 'Psychotherapist'), ('PHT', 'Public Health Technician'), ('RPH', 'Radiologic Technologist'), ('RN', 'Registered Nurse'), ('RT', 'Respiratory Therapist'), ('SCW', 'Social Care Worker'), ('SLT', 'Speech and Language Therapist'), ('SPT', 'Support Worker'), ('SW', 'Social Worker')], default='', max_length=50)),
            ],
        ),
    ]
