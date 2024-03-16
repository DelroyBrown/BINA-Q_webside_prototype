from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "department_name",
        "get_department_type_display",
        "department_id",
        "department_contact_number",
    )

    def get_department_type_display(self, obj):
        return obj.get_department_type_display()

    get_department_type_display.short_description = (
        "Department Type"  # Sets the column name
    )
