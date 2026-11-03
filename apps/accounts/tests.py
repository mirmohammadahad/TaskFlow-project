from django.contrib.staticfiles import finders
from django.test import RequestFactory, SimpleTestCase
from django.urls import reverse

from .views import dashboard


class LoginPageTests(SimpleTestCase):
    def test_login_page_renders_with_static_stylesheet(self):
        response = self.client.get(reverse("accounts:login"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")
        self.assertContains(response, "Welcome back")
        self.assertContains(response, "/static/accounts/login.css")
        self.assertNotContains(response, "Make room for work that matters.")
        self.assertIsNotNone(finders.find("accounts/login.css"))

    def test_login_page_displays_required_field_errors(self):
        response = self.client.post(
            reverse("accounts:login"),
            {"username": "", "password": ""},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")

    def test_django_admin_uses_taskflow_stylesheet(self):
        response = self.client.get("/admin/login/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "/static/accounts/admin.css")
        self.assertIsNotNone(finders.find("accounts/admin.css"))

    def test_admin_role_has_a_renderable_workspace(self):
        request = RequestFactory().get(reverse("accounts:dashboard"))
        request.user = type(
            "AdminUser",
            (),
            {
                "email": "admin@example.com",
                "is_staff": True,
                "get_full_name": lambda self: "TaskFlow Admin",
                "get_role_display": lambda self: "Admin",
            },
        )()

        response = dashboard.__wrapped__(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TaskFlow Admin")
        self.assertContains(response, "/static/accounts/dashboard.css")
        self.assertContains(response, "/admin/")
