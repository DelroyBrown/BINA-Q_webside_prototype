from . import views
from django.urls import path


app_name = "BINA_organisations"

urlpatterns = [
    path("", views.organisation_members_list, name="organisation-members-list"),
]
