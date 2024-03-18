# forms.py
from django import forms
from .models import (
    HealthcareWorker,
    Department,
    Role,
    Organisation,
    HealthcareWorkerPersonalNotes,
)


class OrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = "__all__"


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = "__all__"


class HealthcareWorkerForm(forms.ModelForm):
    class Meta:
        model = HealthcareWorker
        fields = [
            "first_name",
            "other_names",
            "last_name",
            "contact_number",
            "work_email",
            "specialises_in",
            "access_level",
            "ods_code",
        ]


class HealthcareWorkerPersonalNoteForm(forms.ModelForm):
    class Meta:
        model = HealthcareWorkerPersonalNotes
        fields = ["note_text"]
