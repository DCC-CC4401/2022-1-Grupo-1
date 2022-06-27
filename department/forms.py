# django
from django import forms

from .models import Announcement
from .models import Parking
from .models import Visit


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = (
            "department",
            "rut",
            "name",
            "first_last_name",
            "second_last_name",
            "phone",
            "date",
            "check_in",
        )
        widgets = {
            "date": forms.TextInput(attrs={"type": "date"}),
            "check_in": forms.TextInput(attrs={"type": "time"}),
        }


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = (
            "title",
            "description",
            "image",
        )


class AnnouncementChangeForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = (
            "title",
            "description",
        )


class ParkingChangeForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = (
            "department",
            "license_plate",
            "status",
        )
