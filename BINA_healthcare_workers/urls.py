from .views import (
    healthcare_worker_signup,
    user_registered_email_sent,
    healthcare_user_login,
    healthcare_user_profile,
    add_note,
    healthcare_worker_notes,
    healthcare_user_logout,
    custom_password_change,
)
from django.views.generic import TemplateView
from django.urls import path


app_name = "BINA_healthcare_workers"


urlpatterns = [
    path("signup/", healthcare_worker_signup, name="healthcare-worker-signup"),
    path("user-registered/", user_registered_email_sent, name="user-registered"),
    path("login/", healthcare_user_login, name="healthcare-user-login"),
    path("logout/", healthcare_user_logout, name="healthcare-user-logout"),
    path("profile/", healthcare_user_profile, name="healthcare-user-profile"),
    path("notes/", healthcare_worker_notes, name="healthcare-worker-saved-notes"),
    path("add-note/", add_note, name="add_note"),
    path("password_change/", custom_password_change, name="password_change"),
    path(
        "password_change/done/",
        TemplateView.as_view(
            template_name="healthcare_worker_signup/password_change_done.html"
        ),
        name="password_change_done",
    ),
]
