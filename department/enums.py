# django
from django.utils.translation import gettext_lazy as _


class ParkingStatus:
    FREE = "Free"
    OCCUPIED = "Occupied"

    CHOICES = (
        (FREE, _("Free")),
        (OCCUPIED, _("Occupied")),
    )


class ValidationCodeStatus:
    AVAILABLE = "Available"
    USED = "Used"

    CHOICES = (
        (AVAILABLE, _("Available")),
        (USED, _("Used")),
    )
