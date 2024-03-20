import random
import string
from django.db import IntegrityError, transaction
from django.contrib import messages
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
    OrganisationAddressForm,
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
        worker_form = HealthcareWorkerForm(request.POST, request.FILES, prefix="worker")
        department_form = DepartmentForm(request.POST, prefix="dept")
        role_form = RoleForm(request.POST, prefix="role")
        address_form = OrganisationAddressForm(request.POST, prefix="address")

        if all(
            [
                worker_form.is_valid(),
                department_form.is_valid(),
                role_form.is_valid(),
                address_form.is_valid(),
            ]
        ):
            department = department_form.save()
            role = role_form.save()
            address = address_form.save(commit=False)
            address.organisation = worker_form.cleaned_data["organisation"]
            address.save()

            try:
                with transaction.atomic():
                    temp_password = generate_temporary_password()
                    # Generate BINA-Q ID
                    bina_q_id = generate_bina_q_id(
                        worker_form.cleaned_data["first_name"],
                        worker_form.cleaned_data["last_name"],
                        worker_form.cleaned_data[
                            "organisation"
                        ].organisation_name,  # Make sure you can access organisation name like this
                        department.department_name,
                    )
                    # Create the User instance first with BINA-Q ID as the username
                    user = User.objects.create_user(
                        username=bina_q_id,  # Use BINA-Q ID as username
                        email=worker_form.cleaned_data["work_email"],
                        password=temp_password,
                    )

                    worker = worker_form.save(commit=False)
                    worker.department = department
                    worker.role = role
                    worker.user = (
                        user  # Associate the User instance with the HealthcareWorker
                    )
                    worker.bina_q_id = bina_q_id
                    worker.save()

                    # Send email logic here
                    message = f"""New healthcare worker signed up:
                    Name: {worker.first_name} {worker.last_name}
                    Department: {department.department_name}
                    Role: {role.role}
                    Organisation: {worker.organisation.organisation_name}
                    Contact Number: {worker_form.cleaned_data.get("contact_number")}
                    Work Email: {worker_form.cleaned_data.get("work_email")}
                    BINA-Q ID: {worker.bina_q_id}
                    Temporary Password: {temp_password}

                    Please change your password upon first login."""
                    send_mail(
                        "New Healthcare Worker Signup",
                        message,
                        "your_email@example.com",
                        [worker.work_email],
                        fail_silently=False,
                    )

                    return redirect("BINA_healthcare_workers:user-registered")
            except IntegrityError as e:
                # Handle the unique constraint or other database errors
                messages.error(request, "An error occurred. Please try again.")
    else:
        worker_form = HealthcareWorkerForm(prefix="worker")
        department_form = DepartmentForm(prefix="dept")
        role_form = RoleForm(prefix="role")
        address_form = OrganisationAddressForm(prefix="address")

    return render(
        request,
        "healthcare_worker_signup/healthcare_worker_signup.html",
        {
            "worker_form": worker_form,
            "department_form": department_form,
            "role_form": role_form,
            "address_form": address_form,
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
                messages.error(request, "Invalid BINA-Q ID or password.")
        else:
            messages.error(request, "Please correct the errors below.")
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
    notes = request.user.healthcare_worker.notes.all().order_by("-created_at")
    notes_form = HealthcareWorkerPersonalNoteForm()
    latest_note = notes.first()
    formatted_datetime = None
    urgency_level = None

    if latest_note:
        formatted_datetime = date_format(latest_note.created_at, "d F, Y H:i")
        urgency_level = latest_note.note_urgency

    context = {
        "worker": worker,
        "notes": notes,
        "notes_form": notes_form,
        "latest_note": latest_note,
        "urgency_level": urgency_level,
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
    try:
        worker = HealthcareWorker.objects.get(user=request.user)
    except HealthcareWorker.DoesNotExist:
        worker = None
    notes = request.user.healthcare_worker.notes.all().order_by("-created_at")
    context = {
        "worker": worker,
        "notes": notes,
    }

    return render(
        request,
        "healthcare_worker_saved_notes/healthcare_worker_saved_notes.html",
        context,
    )


def healthcare_user_logout(request):
    logout(request)
    return redirect("BINA_healthcare_workers:healthcare-user-login")
