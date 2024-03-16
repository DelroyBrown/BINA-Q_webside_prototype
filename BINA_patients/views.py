from django.shortcuts import render


def patients_list(request):
    return render(request, "patients/patients_list.html")


def patient_detail(request):
    return render(request, "patients/patient_detail.html")
