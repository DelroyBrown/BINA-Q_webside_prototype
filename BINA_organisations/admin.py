from django.contrib import admin
from .models import Organisation


class OrganisationAdmin(admin.ModelAdmin):
    list_display = [
        "organisation_name",
        "ods_code",
        
    ]


admin.site.register(Organisation, OrganisationAdmin)
