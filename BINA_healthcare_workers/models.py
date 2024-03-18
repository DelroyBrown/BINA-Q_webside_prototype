from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from BINA_departments.models import Department
from BINA_organisations.models import Organisation
from BINA_roles.models import Role


class HealthcareWorker(models.Model):
    ACCESS_LEVELS = [
        ("S", "Symptoms"),
        ("RD", "Real-Time Data"),
        ("HI", "Health Information"),
        ("RED", "Recorded Health Data"),
        ("L1B", "Level 1 - Basic"),
        ("L2G", "Level 2 - General"),
        ("L3D", "Level 3 - Detailed"),
        ("XNA", "No Access"),
        ("MA88", "Master Access"),
    ]
    first_name = models.CharField(max_length=100, blank=False, null=False, default="")
    other_names = models.CharField(max_length=100, blank=True, null=True, default="")
    last_name = models.CharField(max_length=100, blank=False, null=False, default="")
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    contact_number = models.CharField(
        max_length=30, blank=False, null=False, default=""
    )
    work_email = models.EmailField(max_length=100, blank=False, null=False, default="")
    ods_code = models.CharField(
        max_length=20, blank=False, null=False, default="AA66TY"
    )
    specialises_in = models.CharField(
        max_length=100, blank=False, null=False, default=""
    )
    access_level = models.CharField(
        choices=ACCESS_LEVELS, max_length=10, blank=False, null=False, default=""
    )
    bina_q_id = models.CharField(max_length=50, blank=True, unique=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="healthcare_worker", default=""
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.department}"


class HealthcareWorkerPersonalNotes(models.Model):
    healthcare_worker = models.ForeignKey(
        HealthcareWorker,
        on_delete=models.CASCADE,
        related_name="notes",
    )
    note_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.healthcare_worker.first_name} {self.healthcare_worker.last_name} on {self.created_at.strftime('%Y-%m-%d')}"
