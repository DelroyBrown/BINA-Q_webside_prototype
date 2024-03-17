from django.shortcuts import render


def organisation_members_list(request):
    return render(request, "organisation/organisation_members_list.html")
