from django.shortcuts import render
from BINA_healthcare_workers.models import HealthcareWorker


def patients_list(request):
    try:
        current_worker = HealthcareWorker.objects.get(user=request.user)
    except HealthcareWorker.DoesNotExist:
        current_worker = None
    return render(request, "patients/patients_list.html", {"current_worker": current_worker})


def patient_detail(request):
    try:
        current_worker = HealthcareWorker.objects.get(user=request.user)
    except HealthcareWorker.DoesNotExist:
        current_worker = None
    return render(request, "patients/patient_detail.html", {"current_worker": current_worker})
