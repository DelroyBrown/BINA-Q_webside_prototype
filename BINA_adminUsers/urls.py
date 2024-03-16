from django.urls import path
from . import views

app_name = "BINA_adminUsers"

urlpatterns = [
    path("", views.admin_home, name="admin-home"),
]
