from django.shortcuts import render
from BINA_healthcare_workers.models import HealthcareWorker


def organisation_members_list(request):
    try:
        worker = HealthcareWorker.objects.get(user=request.user)
    except HealthcareWorker.DoesNotExist:
        worker = None
    return render(
        request, "organisation/organisation_members_list.html", {"worker": worker}
    )
