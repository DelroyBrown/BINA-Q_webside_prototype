from django.contrib import admin
from .models import Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("get_role_display",)

    def get_role_display(self, obj):
        return obj.get_role_display()

    get_role_display.short_description = "Role"
