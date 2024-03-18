import random
import string
from django.utils.formats import date_format
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import JsonResponse
from BINA_organisations.models import Organisation
from django.contrib.auth.decorators import login_required
from .models import HealthcareWorker, HealthcareWorkerPersonalNotes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import (
    HealthcareWorkerForm,
    DepartmentForm,
    RoleForm,
    OrganisationForm,
    HealthcareWorkerPersonalNoteForm,
)


def generate_bina_q_id(first_name, last_name, organisation_name, department_name):
    random_part = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    bina_q_id = f"{first_name[:2].upper()}{last_name[:2].upper()}{organisation_name[:3].upper()}{department_name[:3].upper()}-{random_part}"
    return bina_q_id


def generate_temporary_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for i in range(10))


def healthcare_worker_signup(request):
    if request.method == "POST":
        worker_form = HealthcareWorkerForm(request.POST, prefix="worker")
        department_form = DepartmentForm(request.POST, prefix="dept")
        role_form = RoleForm(request.POST, prefix="role")
        organisation_form = OrganisationForm(request.POST, prefix="org")

        if (
            worker_form.is_valid()
            and department_form.is_valid()
            and role_form.is_valid()
            and organisation_form.is_valid()
        ):
            # Before creating a new organisation, check if it already exists
            org_name = organisation_form.cleaned_data["organisation_name"]
            organisation, created = Organisation.objects.get_or_create(
                organisation_name=org_name
            )

            department = department_form.save(commit=False)
            department.organisation = organisation
            department.save()

            role = role_form.save()

            worker = worker_form.save(commit=False)
            worker.department = department
            worker.role = role
            worker.organisation = organisation
            worker.bina_q_id = generate_bina_q_id(
                worker.first_name,
                worker.last_name,
                organisation.organisation_name,
                department.department_name,
            )

            # Generate a temporary password for the worker
            temporary_password = generate_temporary_password()

            user = User.objects.create_user(
                username=worker.bina_q_id, email=worker.work_email
            )
            user.set_password(temporary_password)
            worker.user = user
            user.save()

            # Ensure to save the healthcare worker after creating the associated user
            worker.save()

            message = (
                f"New healthcare worker signed up:\n\n"
                f"Name: {worker.first_name} {worker.last_name}\n"
                f"Department: {department.department_name} ({department.get_department_type_display()})\n"
                f"Role: {role.get_role_display()}\n"
                f"Organisation: {organisation.organisation_name}\n"
                f"Contact Number: {worker.contact_number}\n"
                f"Work Email: {worker.work_email}\n"
                f"BINA-Q ID: {worker.bina_q_id}\n"
                f"Temporary Password: {temporary_password}\nPlease change your password upon first login."
            )

            send_mail(
                "New Healthcare Worker Signup",
                message,
                "your_email@example.com",
                [worker.work_email],
            )
            return redirect("BINA_healthcare_workers:user-registered")
    else:
        worker_form = HealthcareWorkerForm(prefix="worker")
        department_form = DepartmentForm(prefix="dept")
        role_form = RoleForm(prefix="role")
        organisation_form = OrganisationForm(prefix="org")

    return render(
        request,
        "healthcare_worker_signup/healthcare_worker_signup.html",
        {
            "worker_form": worker_form,
            "department_form": department_form,
            "role_form": role_form,
            "organisation_form": organisation_form,
        },
    )


def user_registered_email_sent(request):
    return render(request, "healthcare_worker_signup/user_registered_email_sent.html")


# HEALTHCARE WORKER PROFILE


def healthcare_user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("BINA_healthcare_workers:healthcare-user-profile")
    else:
        form = AuthenticationForm()
    return render(
        request,
        "healthcare_worker_profile/healthcare_worker_login.html",
        {"form": form},
    )


@login_required
def healthcare_user_profile(request):
    try:
        worker = HealthcareWorker.objects.get(user=request.user)
    except HealthcareWorker.DoesNotExist:
        worker = None

    notes = request.user.healthcare_worker.notes.all()
    notes_form = HealthcareWorkerPersonalNoteForm()
    latest_note = (
        HealthcareWorkerPersonalNotes.objects.filter(
            healthcare_worker=request.user.healthcare_worker
        )
        .order_by("-created_at")
        .first()
    )

    # Initialize formatted_datetime and urgency_level to None outside the if block
    formatted_datetime = None
    urgency_level = None

    if latest_note:
        formatted_datetime = date_format(latest_note.created_at, "d F, Y H:i")
        urgency_level = latest_note.note_urgency  # Assign urgency_level here

    context = {
        "worker": worker,
        "notes": notes,
        "notes_form": notes_form,
        "latest_note": latest_note,
        "urgency_level": urgency_level,  # Use the variable in the context
        "formatted_datetime": formatted_datetime,
    }
    return render(
        request, "healthcare_worker_profile/healthcare_worker_profile.html", context
    )


def add_note(request):
    if request.method == "POST":
        form = HealthcareWorkerPersonalNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.healthcare_worker = request.user.healthcare_worker
            note.save()
            # Format the datetime of note creation
            formatted_datetime = date_format(note.created_at, "d F, Y H:i")
            return JsonResponse(
                {
                    "success": True,
                    "note_text": note.note_text,
                    "created_at": formatted_datetime,
                    "note_urgency": note.get_note_urgency_display(),
                }
            )
        else:
            return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error": "Bad Request"}, status=400)


def healthcare_worker_notes(request):
    return render(
        request, "healthcare_worker_saved_notes/healthcare_worker_saved_notes.html"
    )


from django.contrib.auth import logout


def healthcare_user_logout(request):
    logout(request)
    return redirect("BINA_healthcare_workers:healthcare-user-login")
