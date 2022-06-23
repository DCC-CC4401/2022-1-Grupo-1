# django
from django.utils.translation import gettext_lazy as _


class ParkingStatus:
    FREE = "Libre"
    OCCUPIED = "Ocupado"

    CHOICES = (
        (FREE, _("Libre")),
        (OCCUPIED, _("Ocupado")),
    )


class ValidationCodeStatus:
    AVAILABLE = "Available"
    USED = "Used"

    CHOICES = (
        (AVAILABLE, _("Available")),
        (USED, _("Used")),
    )
