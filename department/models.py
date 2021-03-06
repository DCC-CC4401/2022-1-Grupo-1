# django
from django.db import models
from django.urls import reverse
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
    )
    check_in = models.TimeField(
        _("check in"),
    )

    class Meta:
        verbose_name = _("visit")
        verbose_name_plural = _("visits")
        ordering = ["-date", "-check_in"]

    def __str__(self):
        return f"{self.name} {self.first_last_name} {self.second_last_name}"

    def get_absolute_url(self):
        return reverse("visit_list")


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
        auto_now_add=True,
    )
    title = models.CharField(
        _("title"),
        max_length=255,
    )
    description = models.TextField(
        _("description"),
    )
    image = models.ImageField(
        verbose_name=_("image"),
        upload_to=file_path,
    )

    class Meta:
        verbose_name = _("announcement")
        verbose_name_plural = _("announcements")

    @property
    def short_description(self, length=100):
        short_description = self.description[:length]
        if len(self.description) > length:
            short_description += "..."
        return short_description

    def get_absolute_url(self):
        return reverse("announcement_detail", args=(self.pk,))

    def __str__(self):
        return f"{self.title} {self.date}"


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

    class Meta:
        verbose_name = _("parking")
        verbose_name_plural = _("parkings")

    def get_absolute_url(self):
        return reverse("parking_list")


class Department(models.Model):
    """Model that represents a department"""

    number = models.IntegerField(
        _("number"),
    )

    class Meta:
        verbose_name = _("department")
        verbose_name_plural = _("departments")

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

    class Meta:
        verbose_name = _("validation code")
        verbose_name_plural = _("validation codes")

    def use(self, user):
        self.user = user
        self.status = ValidationCodeStatus.USED
        self.save()
