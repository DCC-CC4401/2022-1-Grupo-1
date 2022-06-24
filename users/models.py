# django
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Class that represents a user
    """

    rut = models.CharField(
        _("rut"),
        max_length=13,
        unique=True,
    )
    email = models.EmailField(
        _("email"),
        unique=True,
    )
    name = models.CharField(
        _("name"),
        max_length=50,
    )
    first_last_name = models.CharField(
        _("first last name"),
        max_length=50,
    )
    second_last_name = models.CharField(
        _("second last name"),
        max_length=50,
    )
    phone = models.CharField(
        _("phone"),
        max_length=13,
    )
    department = models.ForeignKey(
        "department.Department",
        on_delete=models.CASCADE,
        verbose_name=_("department"),
        related_name="habitants",
        blank=True,
        null=True,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "rut",
        "name",
        "first_last_name",
        "second_last_name",
        "phone",
    ]

    is_active = models.BooleanField(
        default=True,
    )
    admin = models.BooleanField(
        default=False,
    )

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_full_name(self):
        # Returns the full name of the user
        return f"{self.name} {self.first_last_name} {self.second_last_name}"

    def get_short_name(self):
        return f"{self.name} {self.first_last_name}"

    def __str__(self):
        return self.get_full_name()

    @property
    def is_staff(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.admin

    def save(self, *args, **kwargs):
        """Normalize email address on change"""
        self.email = UserManager.normalize_email(self.email)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("profile")
