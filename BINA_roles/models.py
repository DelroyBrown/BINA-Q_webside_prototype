from django.db import models


class Role(models.Model):
    ROLES = [
        ("AHP", "Allied Health Professional"),
        ("HA", "Healthcare Administrator"),
        ("HCA", "Healthcare Assistant"),
        ("MGT", "Healthcare Manager"),
        ("HCW", "Healthcare Worker"),
        ("HR", "Hospital Receptionist"),
        ("LAC", "Lactation Consultant"),
        ("LPN", "Licensed Practical Nurse"),
        ("MA", "Medical Assistant"),
        ("MAA", "Medical Administrative Assistant"),
        ("MOA", "Medical Office Assistant"),
        ("MS", "Medical Secretary"),
        ("MD", "Medical Doctor"),
        ("MT", "Medical Technologist"),
        ("MHN", "Mental Health Nurse"),
        ("NP", "Nurse Practitioner"),
        ("OT", "Occupational Therapist"),
        ("PA", "Physician Assistant"),
        ("PC", "Patient Coordinator"),
        ("PH", "Pharmacist"),
        ("PT", "Physical Therapist"),
        ("PTA", "Physical Therapist Assistant"),
        ("PCN", "Primary Care Nurse"),
        ("PSY", "Psychiatrist"),
        ("CPS", "Child Psychologist"),
        ("CNS", "Clinical Nurse Specialist"),
        ("CP", "Clinical Psychologist"),
        ("CHN", "Community Health Nurse"),
        ("CA", "Clinic Administrator"),
        ("CCO", "Care Coordinator"),
        ("CNA", "Certified Nursing Assistant"),
        ("DT", "Dietitian"),
        ("EMS", "Emergency Medical Technician"),
        ("GEN", "Genetic Counselor"),
        ("HIT", "Health Information Technician"),
        ("HSM", "Health Services Manager"),
        ("PSYT", "Psychotherapist"),
        ("PHT", "Public Health Technician"),
        ("RPH", "Radiologic Technologist"),
        ("RN", "Registered Nurse"),
        ("RT", "Respiratory Therapist"),
        ("SCW", "Social Care Worker"),
        ("SLT", "Speech and Language Therapist"),
        ("SPT", "Support Worker"),
        ("SW", "Social Worker"),
    ]
    role = models.CharField(
        choices=ROLES, max_length=50, blank=False, null=False, default=""
    )

    def __str__(self):
        return self.role

    def get_role_display(self):
        return dict(Role.ROLES)[self.role]
