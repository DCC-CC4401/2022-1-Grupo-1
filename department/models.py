# django
from django.db import models
from django.urls import reverse
from django.utils import timezone

from base.models import file_path
from users.models import User


# Create your models here.
class Visit(models.Model):
    """Model that represents a visit"""

    # TODO: add department foreign key when department model is created
    rut = models.CharField(
        verbose_name="rut",
        max_length=13,
    )
    name = models.CharField(
        verbose_name="name",
        max_length=50,
    )
    first_last_name = models.CharField(
        verbose_name="first last name",
        max_length=50,
    )
    second_last_name = models.CharField(
        verbose_name="second last name",
        max_length=50,
    )
    phone = models.CharField(
        verbose_name="phone",
        max_length=13,
    )
    date = models.DateField(
        verbose_name="date",
        default=timezone.now,
    )
    check_in = models.TimeField(
        verbose_name="check in",
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
        related_name="announcements",
    )
    date = models.DateField(
        verbose_name="date",
        default=timezone.now,
    )
    title = models.CharField(
        verbose_name="title",
        max_length=255,
    )
    description = models.TextField(
        verbose_name="description",
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
        return f"Anuncio: {self.title}"


class Parking(models.Model):
    """Model for parking table"""

    status = models.CharField(
        verbose_name="Status",
        max_length=10
        # ver lo de las opciones
    )

    number = models.IntegerField(
        verbose_name="Parking space number"
        # Ver que solo sea una cantidad definida
    )

    # TODO: agregar atrib department

    license_plate = models.CharField(
        verbose_name="license plate",
        max_length=8,
        blank=True,
    )
