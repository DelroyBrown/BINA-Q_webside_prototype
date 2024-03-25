import os
import json
from django.conf import settings
from django.db import models


def load_role_types():
    path = os.path.join(settings.BASE_DIR, "BINA_roles", "roles.json")
    with open(path, "r") as file:
        return json.load(file)


ROLES = [(dept["code"], dept["name"]) for dept in load_role_types()]


class Role(models.Model):
    role = models.CharField(
        choices=ROLES, max_length=50, blank=False, null=False, default=""
    )

    def get_role_display(self):
        return dict(ROLES)[self.role]

    def __str__(self):
        return self.get_role_display()
