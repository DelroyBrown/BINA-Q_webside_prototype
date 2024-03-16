from django.db import models
from BINA_departments.models import Department
from BINA_organisations.models import Organisation
from BINA_roles.models import Role


class AdminUser(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False, default="")
    other_names = models.CharField(max_length=200, blank=True, null=True, default="")
    last_name = models.CharField(max_length=50, blank=False, null=False, default="")
    organisation_you_work_for = models.ForeignKey(
        Organisation, on_delete=models.CASCADE
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    personal_ods_code = models.CharField(
        blank=False, null=False, max_length=10, default="A12345"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"
