# Generated by Django 5.0.3 on 2024-03-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BINA_departments', '0002_alter_department_department_contact_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_type',
            field=models.CharField(choices=[('ACC', 'Accident & Emergency'), ('ADM', 'Administration'), ('ALL', 'Allergy & Immunology'), ('AMB', 'Ambulance Services'), ('ANA', 'Anesthesiology'), ('AUD', 'Audiology'), ('BEH', 'Behavioral Health'), ('BIO', 'Biochemistry'), ('BLD', 'Blood Bank'), ('BMT', 'Bone Marrow Transplant'), ('BRN', 'Breast Cancer'), ('CAR', 'Cardiac Rehabilitation'), ('CHM', 'Chemotherapy'), ('CLN', 'Clinical Services'), ('CRD', 'Cardiology'), ('CRT', 'Cardiac Surgery'), ('DEN', 'Dentistry'), ('DER', 'Dermatology'), ('DIA', 'Diabetic Care'), ('DIE', 'Dietetics'), ('DVA', 'Diagnostic Imaging'), ('EAR', 'Ear, Nose & Throat'), ('ECG', 'Electrocardiography'), ('EMR', 'Emergency Medicine'), ('EMT', 'Emergency Medical Technicians'), ('END', 'Endocrinology'), ('EPL', 'Epilepsy'), ('FER', 'Fertility Services'), ('GAS', 'Gastroenterology'), ('GEN', 'General Practice'), ('GER', 'Geriatrics'), ('GYN', 'Gynecology'), ('HEM', 'Hematology'), ('HEP', 'Hepatology'), ('HOS', 'Hospice Care'), ('HPV', 'Human Papillomavirus'), ('HRM', 'Human Resources Management'), ('ICU', 'Intensive Care Unit'), ('IFD', 'Infectious Diseases'), ('INF', 'Infertility Services'), ('INR', 'Inpatient Rehabilitation'), ('INT', 'Internal Medicine'), ('IVF', 'In Vitro Fertilization'), ('LAB', 'Laboratory Services'), ('LTC', 'Long-Term Care'), ('LYM', 'Lymphology'), ('MAM', 'Mammography'), ('MED', 'Medical Records'), ('MEN', 'Mental Health'), ('MTN', 'Maternity Services'), ('NEO', 'Neonatology'), ('NEP', 'Nephrology'), ('NEU', 'Neurology'), ('NTR', 'Nutrition Services'), ('NUC', 'Nuclear Medicine'), ('OBG', 'Obstetrics & Gynecology'), ('ONC', 'Oncology'), ('ONR', 'Oncology Radiotherapy'), ('OPH', 'Ophthalmology'), ('OPT', 'Optometry'), ('ORT', 'Orthopedics'), ('OST', 'Osteopathy'), ('OTH', 'Otolaryngology'), ('OTO', 'Otology'), ('OXY', 'Oxygen Therapy'), ('PAL', 'Palliative Care'), ('PAR', 'Paramedics'), ('PAT', 'Pathology'), ('PDE', 'Pediatric Dentistry'), ('PED', 'Pediatrics'), ('PHM', 'Pharmaceutical Services'), ('PHY', 'Physiotherapy'), ('PLN', 'Planning & Management'), ('PLT', 'Plastic Surgery'), ('PMR', 'Physical Medicine & Rehabilitation'), ('POD', 'Podiatry'), ('PRE', 'Preventive Medicine'), ('PRM', 'Premises Management'), ('PSY', 'Psychiatry'), ('PSYA', 'Psychiatric Assessment'), ('PSYC', 'Psychiatric Counseling'), ('PSYT', 'Psychiatric Therapy'), ('PTH', 'Pathology'), ('PUL', 'Pulmonology'), ('RAD', 'Radiology'), ('RDT', 'Radiotherapy'), ('REN', 'Renal Care'), ('RES', 'Respiratory Care'), ('RHB', 'Rehabilitation Services'), ('RHM', 'Rheumatology'), ('SLP', 'Speech-Language Pathology'), ('SOC', 'Social Services'), ('SPI', 'Spinal Cord Injury'), ('SPM', 'Sports Medicine'), ('SUR', 'Surgery'), ('THR', 'Therapeutic Radiology'), ('TRA', 'Transplant Services'), ('TRU', 'Trauma Services'), ('URO', 'Urology'), ('VAS', 'Vascular Surgery'), ('VIR', 'Virology'), ('WMN', "Women's Health"), ('WND', 'Wound Care'), ('GNT', 'Genetics'), ('IMG', 'Imaging Services'), ('IMM', 'Immunology'), ('INF', 'Infectious Disease'), ('LVR', 'Liver Transplant'), ('MAS', 'Mastectomy Services'), ('MOB', 'Mobile Health Services'), ('NRO', 'Neuro-Oncology'), ('NRS', 'Nursing Services'), ('OBS', 'Obstetrics'), ('ONC', 'Oncology'), ('OPR', 'Operating Rooms'), ('OSC', 'Ostomy Care'), ('PAI', 'Pain Management'), ('PAL', 'Palliative Care'), ('PCC', 'Patient Care Coordinators'), ('PED', 'Pediatric Intensive Care Unit'), ('PHS', 'Physical Therapy'), ('PLN', 'Planning & Management'), ('PRT', 'Prosthetics & Orthotics'), ('RDN', 'Radiation Oncology'), ('RHB', 'Rehabilitation Services'), ('RHM', 'Rheumatology'), ('SLP', 'Speech-Language Pathology'), ('SNF', 'Skilled Nursing Facility'), ('STR', 'Stroke Services'), ('TRA', 'Transplant Services'), ('URG', 'Urgent Care'), ('WND', 'Wound Care')], default='', max_length=50),
        ),
    ]
