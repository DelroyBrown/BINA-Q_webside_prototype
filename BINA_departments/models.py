import os
import json
from django.conf import settings
from django.db import models


# Load department types from JSON file
def load_department_types():
    path = os.path.join(settings.BASE_DIR, "BINA_departments", "department_types.json")
    with open(path, "r") as file:
        return json.load(file)


# Convert to the format Django expects: [('code', 'name'), ...]
DEPARTMENT_TYPES = [(dept["code"], dept["name"]) for dept in load_department_types()]
class Department(models.Model):
    department_name = models.CharField(
        blank=False, null=False, max_length=100, default=""
    )
    department_type = models.CharField(
        choices=DEPARTMENT_TYPES, max_length=50, blank=False, null=False, default=""
    )
    department_id = models.CharField(
        max_length=20, blank=False, null=False, default=""
    )
    department_contact_number = models.CharField(
        max_length=100, blank=True, null=True, default=""
    )

    def get_department_type_display(self):
        return dict(DEPARTMENT_TYPES)[self.department_type]

    def __str__(self):
        return self.get_department_type_display()
