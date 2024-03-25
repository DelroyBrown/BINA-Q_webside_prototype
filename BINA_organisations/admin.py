from django.contrib import admin
from .models import Organisation, OrganisationAddress


class OrganisationAdmin(admin.ModelAdmin):
    list_display = [
        "organisation_name",
        "ods_code",
        
    ]

class OrganisationAddressAdmin(admin.ModelAdmin):
    list_display = [
        "organisation",
        "building_name_or_number",
        "street",
        "town_or_city",
        "county",
        "postcode",
        "country",
        
    ]


admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(OrganisationAddress, OrganisationAddressAdmin)
