# BINA_patients/views.py
from django.shortcuts import render
from BINA_healthcare_workers.models import HealthcareWorker
from django.http import JsonResponse
from .firebase_config import get_all_users


def get_firebase_data(request):
    users_data = get_all_users()
    return JsonResponse(users_data, safe=False)


def patients_list(request):
    try:
        current_worker = HealthcareWorker.objects.get(user=request.user)
    except HealthcareWorker.DoesNotExist:
        current_worker = None
    return render(
        request, "patients/patients_list.html", {"current_worker": current_worker}
    )


def patient_detail(request):
    try:
        current_worker = HealthcareWorker.objects.get(user=request.user)
    except HealthcareWorker.DoesNotExist:
        current_worker = None
    return render(
        request, "patients/patient_detail.html", {"current_worker": current_worker}
    )
