
"""
URL configuration for TaskFlow project.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django Admin Panel
    path("admin/", admin.site.urls),

    # TaskFlow Authentication (Login, Logout, Dashboard)
    path("accounts/", include("apps.accounts.urls")),
]
