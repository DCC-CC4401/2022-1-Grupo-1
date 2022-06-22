# django
from django.contrib import admin

from .models import Announcement
from .models import Parking
from .models import Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    pass


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    pass


@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    pass
