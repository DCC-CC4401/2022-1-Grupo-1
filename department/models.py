# django
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from base.models import file_path
from users.models import User

from .enums import ParkingStatus
from .enums import ValidationCodeStatus
from .utils import create_validation_code


# Create your models here.
class Visit(models.Model):
    """Model that represents a visit"""

    department = models.ForeignKey(
        "Department",
        on_delete=models.CASCADE,
        verbose_name=_("department"),
        related_name="visits",
    )
    rut = models.CharField(
        _("rut"),
        max_length=13,
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
    date = models.DateField(
        _("date"),
        default=timezone.now,
    )
    check_in = models.TimeField(
        _("check in"),
        default=timezone.now,
    )

    def get_absolute_url(self):
        # TODO: change this when detail view available
        return reverse("home")


class Announcement(models.Model):
    """Model that represents an Announcement"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        related_name="announcements",
    )
    date = models.DateField(
        _("date"),
        default=timezone.now,
    )
    title = models.CharField(
        _("title"),
        max_length=255,
    )
    description = models.TextField(
        _("description"),
    )
    image = models.ImageField(
        upload_to=file_path,
    )

    @property
    def short_description(self, length=100):
        short_description = self.description[:length]
        if len(self.description) > length:
            short_description += "..."
        return short_description

    def get_absolute_url(self):
        # TODO: change this when detail view available
        return reverse("announcement_detail", args=(self.pk,))

    def __str__(self):
        return f"{_('Announcement')}: {self.title}"


class Parking(models.Model):
    """Model for parking table"""

    status = models.CharField(
        _("status"),
        max_length=10,
        choices=ParkingStatus.CHOICES,
    )
    number = models.IntegerField(
        _("parking space number"),
    )
    department = models.ForeignKey(
        "Department",
        on_delete=models.CASCADE,
        verbose_name=_("department"),
        related_name="parkings",
        blank=True,
        null=True,
    )
    license_plate = models.CharField(
        _("license plate"),
        max_length=8,
        blank=True,
    )

    def get_absolute_url(self):
        return reverse("parking_list")


class Department(models.Model):
    """Model that represents a department"""

    number = models.IntegerField(
        _("number"),
    )

    def __str__(self):
        return str(self.number)


class ValidationCode(models.Model):
    """Model that representa a validation code for the doormans"""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        related_name="validation_code",
        blank=True,
        null=True,
    )
    code = models.CharField(
        _("code"),
        max_length=10,
        default=create_validation_code,
    )
    status = models.CharField(
        _("status"),
        max_length=10,
        choices=ValidationCodeStatus.CHOICES,
    )

    def use(self, user):
        self.status = ValidationCodeStatus.USED
        self.user = user
        self.save()
