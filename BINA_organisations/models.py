from django.db import models



class Organisation(models.Model):
    organisation_name = models.CharField(max_length=100)
    ods_code = models.CharField(max_length=25, unique=True)
    organisation_logo = models.ImageField(
        upload_to="organisation_logos/", null=True, blank=True
    )

    def __str__(self):
        return self.organisation_name


class OrganisationAddress(models.Model):
    organisation = models.ForeignKey(
        Organisation, related_name="addresses", on_delete=models.CASCADE
    )
    building_name_or_number = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    town_or_city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=False, null=False, default="")
    
    def __str__(self):
        return self.organisation
