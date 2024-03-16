from .views import patients_list, patient_detail
from django.urls import path


app_name = "BINA_patients"


urlpatterns = [
    path("", patients_list, name="patients-list"),
    path('patient-detail/', patient_detail, name='patient-detail'),
]
