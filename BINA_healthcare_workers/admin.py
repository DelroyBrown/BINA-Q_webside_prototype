from django.contrib import admin
from .models import HealthcareWorker, HealthcareWorkerPersonalNotes

admin.site.register(HealthcareWorkerPersonalNotes)



class HealthcareWorkerAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'other_names',
        'last_name',
        'role',
        'department',
        'organisation',
        'contact_number',
        'access_level',
        'bina_q_id',
    ]

admin.site.register(HealthcareWorker, HealthcareWorkerAdmin)
