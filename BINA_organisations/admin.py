from django.contrib import admin
from .models import Organisation


class OrganisationAdmin(admin.ModelAdmin):
    list_display = [
        "organisation_name",
        "building_name_or_number",
        "street",
        "town_or_city",
        "county",
        "postcode",
        "country",
        
    ]


admin.site.register(Organisation, OrganisationAdmin)
