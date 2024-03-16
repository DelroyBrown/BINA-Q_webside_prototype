from django.db import models


class Organisation(models.Model):
    organisation_name = models.CharField(
        max_length=100, blank=False, null=False, default=""
    )
    building_name_or_number = models.CharField(
        max_length=100, blank=False, null=False, default=""
    )
    street = models.CharField(max_length=100, blank=False, null=False, default="")
    town_or_city = models.CharField(max_length=100, blank=False, null=False, default="")
    county = models.CharField(max_length=100, blank=False, null=False, default="")
    postcode = models.CharField(max_length=100, blank=False, null=False, default="")
    country = models.CharField(max_length=100, blank=False, null=False, default="")
    ods_code = models.CharField(max_length=25, blank=False, null=False, default="")

    def __str__(self):
        return self.organisation_name
