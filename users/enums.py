# django
from django.utils.translation import gettext as _


class UserType:
    HABITANT = "Habitant"
    DOORMAN = "Doorman"

    CHOICES = (
        (HABITANT, _("Habitant")),
        (DOORMAN, _("Doorman")),
    )
