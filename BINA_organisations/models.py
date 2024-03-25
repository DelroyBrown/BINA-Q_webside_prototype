import os
import json
from django.conf import settings
from django.db import models


# THIS MODEL IS ATTACHED TO A JSON FILE FOUND IN THE FIXTURES FOLDER
class Organisation(models.Model):
    organisation_name = models.CharField(max_length=100)
    ods_code = models.CharField(max_length=25, unique=True)
    organisation_logo = models.ImageField(
        upload_to="organisation_logos/", null=True, blank=True
    )

    def __str__(self):
        return self.organisation_name


# Load department types from JSON file
def load_organisation_countries():
    path = os.path.join(
        settings.BASE_DIR, "BINA_organisations", "organisation_countries.json"
    )
    with open(path, "r") as file:
        return json.load(file)


ORGANISATION_COUNTRIES = [
    (dept["code"], dept["name"]) for dept in load_organisation_countries()
]


class OrganisationAddress(models.Model):
    organisation = models.ForeignKey(
        Organisation, related_name="addresses", on_delete=models.CASCADE
    )
    building_name_or_number = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    town_or_city = models.CharField(max_length=100)
    county = models.CharField(max_length=100, blank=True, null=True, default="")
    postcode = models.CharField(max_length=100)
    country = models.CharField(
        choices=ORGANISATION_COUNTRIES,
        blank=False,
        null=False,
        max_length=100,
        default="",
    )

    def __str__(self):
        return self.street
