# BINA_healthcare_workers/views.py
import random
import string
import logging
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from BINA_healthcare_workers.utils.utils import Utils
from django.db import IntegrityError, transaction
from django.contrib import messages
from django.utils.formats import date_format
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.http import JsonResponse
from BINA_organisations.models import Organisation
from django.contrib.auth.decorators import login_required
from .models import HealthcareWorker, HealthcareWorkerPersonalNotes
from BINA_organisations.models import ORGANISATION_COUNTRIES
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from .forms import (
    HealthcareWorkerForm,
    DepartmentForm,
    RoleForm,
    OrganisationForm,
    HealthcareWorkerPersonalNoteForm,
    OrganisationAddressForm,
    CustomPasswordChangeForm,
)

logger = logging.getLogger(__name__)


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
            try:
                with transaction.atomic():
                    # Save department, role, and address first
                    department = department_form.save()
                    role = role_form.save()
                    address = address_form.save(commit=False)
                    address.organisation = worker_form.cleaned_data["organisation"]
                    address.save()

                    # Generate temporary password and BINA-Q ID
                    temp_password = Utils.generate_temporary_password()
                    bina_q_id = Utils.generate_bina_q_id(
                        worker_form.cleaned_data["first_name"],
                        worker_form.cleaned_data["last_name"],
                        worker_form.cleaned_data["organisation"].organisation_name,
                        department.department_name,
                    )

                    # Create the User instance
                    user = User.objects.create_user(
                        username=bina_q_id,
                        email=worker_form.cleaned_data["work_email"],
                        password=temp_password,
                    )

                    # Now, save the HealthcareWorker instance
                    worker = worker_form.save(commit=False)
                    worker.department = department
                    worker.role = role
                    worker.user = user
                    worker.bina_q_id = bina_q_id
                    worker.temp_password_used = False  # Ensure it's set correctly here
                    worker.save()

                    # Email sending logic
                    html_content = render_to_string(
                        "healthcare_worker_signup/emails/user_signedup_email.html",
                        {
                            "worker": worker,
                            "department": department,
                            "role": role,
                            "temp_password": temp_password,
                        },
                    )
                    text_content = strip_tags(html_content)
                    email = EmailMessage(
                        "New Healthcare Worker Signup",
                        html_content,
                        "your_email@example.com",
                        [worker.work_email],
                    )
                    email.content_subtype = "html"
                    email.send()

                    return redirect("BINA_healthcare_workers:user-registered")
            except IntegrityError as e:
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
            "organisation_countries": ORGANISATION_COUNTRIES,
        },
    )


def user_registered_email_sent(request):
    return render(request, "healthcare_worker_signup/user_registered_email_sent.html")


def custom_password_change(request):
    logger.info("Password change form submitted")
    if request.method == "POST":
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            logger.info("Form is valid, proceeding with password change")
            user = form.save()
            update_session_auth_hash(
                request, user
            )  # Keep the user logged in after changing the password

            # Retrieve the HealthcareWorker instance and update temp_password_used
            worker = HealthcareWorker.objects.get(user=user)
            worker.temp_password_used = True
            worker.save()

            logger.info(
                f"Password for user {user.username} changed successfully. temp_password_used set to True."
            )
            messages.success(request, "Your password was successfully updated!")
            return redirect("BINA_healthcare_workers:password_change_done")
        else:
            messages.error(request, "Please correct the errors below.")
            logger.warning("Form is invalid: " + str(form.errors))
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(
        request, "healthcare_worker_signup/custom_password_change.html", {"form": form}
    )


# HEALTHCARE WORKER PROFILE


def healthcare_user_login(request):
    logger.info("Login form submitted")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            logger.info("Login form is valid")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                try:
                    worker = HealthcareWorker.objects.get(user=user)
                    logger.info(f"User {username} authenticated successfully")
                    # Check if the user is logging in with the temp password for the first time
                    if not worker.temp_password_used:
                        worker.temp_password_used = True
                        worker.save()
                        logger.info(
                            f"User {username} is logging in with temp password, redirecting to change password"
                        )
                        login(request, user)
                        # Redirect the user to change their temp password
                        return redirect("BINA_healthcare_workers:password_change")
                    else:
                        # User has already changed the password, proceed with normal login
                        logger.info(
                            f"User {username} has already changed the temp password, proceeding with login"
                        )
                        login(request, user)
                        # Redirect to the user's profile page or another appropriate page
                        return redirect(
                            "BINA_healthcare_workers:healthcare-user-profile"
                        )
                except HealthcareWorker.DoesNotExist:
                    logger.error(
                        f"No HealthcareWorker instance found for user {username}"
                    )
                    messages.error(request, "No corresponding healthcare worker found.")
                    return render(
                        request,
                        "healthcare_worker_profile/healthcare_worker_login.html",
                        {"form": form},
                    )
            else:
                logger.error(f"Invalid login attempt for username {username}")
                messages.error(request, "Invalid username or password.")
        else:
            logger.warning(f"Login form is invalid: {form.errors}")
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
