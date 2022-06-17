# django
from django.contrib import admin

from .models import Announcement, Parking, Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    pass

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    pass

@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    pass
