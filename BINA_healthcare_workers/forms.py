# forms.py
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from BINA_organisations.models import OrganisationAddress
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


class OrganisationAddressForm(forms.ModelForm):
    class Meta:
        model = OrganisationAddress
        exclude = ["organisation"]  # Exclude the organisation field


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = "__all__"


class HealthcareWorkerForm(forms.ModelForm):
    organisation = forms.ModelChoiceField(
        queryset=Organisation.objects.all(), required=True, label="Organisation"
    )

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
            "organisation",
        ]


class HealthcareWorkerPersonalNoteForm(forms.ModelForm):
    class Meta:
        model = HealthcareWorkerPersonalNotes
        fields = ["note_text", "note_urgency"]


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")
