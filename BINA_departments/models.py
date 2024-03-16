from django.db import models


class Department(models.Model):
    DEPARTMENT_TYPES = [
        ("ADM", "Administration"),
        ("CLN", "Clinical Services"),
        ("CRD", "Cardiology"),
        ("DER", "Dermatology"),
        ("END", "Endocrinology"),
        ("GAS", "Gastroenterology"),
        ("GER", "Geriatrics"),
        ("HEM", "Hematology"),
        ("INF", "Infectious Diseases"),
        ("MEN", "Mental Health"),
        ("NEU", "Neurology"),
        ("ONC", "Oncology"),
        ("PED", "Pediatrics"),
        ("PSY", "Psychiatry"),
        ("RAD", "Radiology"),
        ("SUR", "Surgery"),
        ("URO", "Urology"),
    ]
    department_name = models.CharField(
        blank=False, null=False, max_length=100, default=""
    )
    department_type = models.CharField(
        choices=DEPARTMENT_TYPES, max_length=50, blank=False, null=False, default=""
    )
    department_id = models.CharField(
        max_length=20, blank=False, null=False, default="CRD-001"
    )
    department_contact_number = models.CharField(
        max_length=100, blank=True, null=True, default="07795128311"
    )

    def get_department_type_display(self):
        return dict(Department.DEPARTMENT_TYPES)[self.department_type]

    def __str__(self):
        return self.get_department_type_display()
