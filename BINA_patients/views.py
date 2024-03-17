from django.shortcuts import render
from BINA_healthcare_workers.models import HealthcareWorker


def patients_list(request):
    try:
        worker = HealthcareWorker.objects.get(user=request.user)
    except HealthcareWorker.DoesNotExist:
        worker = None
    return render(request, "patients/patients_list.html", {"worker": worker})


def patient_detail(request):
    try:
        worker = HealthcareWorker.objects.get(user=request.user)
    except HealthcareWorker.DoesNotExist:
        worker = None
    return render(request, "patients/patient_detail.html", {"worker": worker})
