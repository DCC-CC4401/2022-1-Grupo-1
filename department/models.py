# django
from django.db import models
from django.utils import timezone


# Create your models here.
class Visit(models.Model):
    """Model thath represents a visit"""

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
