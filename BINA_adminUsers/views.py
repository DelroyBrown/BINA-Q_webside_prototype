from django.shortcuts import render


def admin_home(request):
    return render(request, "home/home.html")
