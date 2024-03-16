from django.contrib import admin
from django.urls import path, include

app_name = "BINAQ_base"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("BINA_adminUsers.urls")),
    path("departments/", include("BINA_departments.urls")),
    path("healthcare_workers/", include("BINA_healthcare_workers.urls")),
    path("organisations/", include("BINA_organisations.urls")),
    path("roles/", include("BINA_roles.urls")),
    path("patients/", include("BINA_patients.urls")),
]
