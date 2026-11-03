
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import TaskFlowLoginForm


class TaskFlowLoginView(LoginView):
    """
    Handles authentication for all three user roles.
    """

    template_name = "accounts/login.html"
    authentication_form = TaskFlowLoginForm

    # Send authenticated users to their dashboard.
    def get_success_url(self):
        return reverse_lazy("accounts:dashboard")


class TaskFlowLogoutView(LogoutView):
    """
    Secure logout endpoint.
    """

    next_page = reverse_lazy("accounts:login")


@login_required
def dashboard(request):
    """
    Display the workspace for the logged-in user.
    """

    user = request.user

    return render(
        request,
        "accounts/dashboard.html",
        {
            "role_label": user.get_role_display(),
            "user_name": user.get_full_name() or user.email,
        },
    )
