
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom manager for TaskFlow User model.

    Handles normal user and superuser creation.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a normal user using email and password.
        """

        # Email is required for every user account.
        if not email:
            raise ValueError("Email address is required.")

        # Normalize email before saving.
        email = self.normalize_email(email)

        # Create a user instance without saving it yet.
        user = self.model(
            email=email,
            **extra_fields
        )

        # Hash the password securely.
        user.set_password(password)

        # Save user using the selected database.
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create an admin-level superuser for Django administration.
        """

        # Superuser must have staff and superuser permissions.
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        # Prevent creating an incorrectly configured superuser.
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            email=email,
            password=password,
            **extra_fields
        )
