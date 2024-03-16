from .views import (
    healthcare_worker_signup,
    user_registered_email_sent,
    healthcare_user_login,
    healthcare_user_profile,
)
from django.urls import path


app_name = "BINA_healthcare_workers"


urlpatterns = [
    path("signup/", healthcare_worker_signup, name="healthcare_worker_signup"),
    path("user-registered/", user_registered_email_sent, name="user-registered"),
    path("login/", healthcare_user_login, name="healthcare-user-login"),
    path("profile/", healthcare_user_profile, name="healthcare-user-profile"),
    # ... other url patterns
]
