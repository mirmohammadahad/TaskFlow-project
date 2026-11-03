
from django.contrib import admin

from .models import User


@admin.register(User)
class TaskFlowUserAdmin(admin.ModelAdmin):

    # Show important user information in the list.
    list_display = (
        "email",
        "first_name",
        "last_name",
        "role",
        "is_active",
    )

    # Allow filtering users by role and account status.
    list_filter = ("role", "is_active")

    # Enable searching by email and name.
    search_fields = ("email", "first_name", "last_name")

    # Do not allow editing password hashes directly.
    readonly_fields = (
        "id",
        "password",
        "last_login",
        "date_joined",
    )

    # Organize user fields in the admin detail page.
    fields = (
        "id",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_active",
        "is_staff",
        "is_superuser",
        "password",
        "last_login",
        "date_joined",
    )

    # User creation will be handled through a secure workflow.
    def has_add_permission(self, request):
        return False
