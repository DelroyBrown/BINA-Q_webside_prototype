from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from BINA_healthcare_workers.models import HealthcareWorker


@login_required
def organisation_members_list(request):
    try:
        current_worker = HealthcareWorker.objects.get(user=request.user)
        organisation_members = HealthcareWorker.objects.filter(
            organisation=current_worker.organisation
        ).exclude(user=request.user)
    except HealthcareWorker.DoesNotExist:
        current_worker = None
        organisation_members = None

    return render(
        request,
        "organisation/organisation_members_list.html",
        {
            "current_worker": current_worker,
            "organisation_members": organisation_members,
        },
    )
