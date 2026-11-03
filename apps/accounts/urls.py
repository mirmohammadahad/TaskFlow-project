
from django.urls import path

from .views import (
    TaskFlowLoginView,
    TaskFlowLogoutView,
    dashboard,
)

app_name = "accounts"

urlpatterns = [
    # Login page
    path("login/", TaskFlowLoginView.as_view(), name="login"),

    # Logout endpoint (POST request)
    path("logout/", TaskFlowLogoutView.as_view(), name="logout"),

    # Role-based dashboard
    path("dashboard/", dashboard, name="dashboard"),
]
