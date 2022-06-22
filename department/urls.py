# django
from django.urls import include
from django.urls import path

from . import views

visit_urlpatterns = [
    path(
        "create/",
        views.VisitCreateView.as_view(),
        name="visit_create",
    ),
]

announcement_urlpatterns = [
    path(
        "create/",
        views.AnnouncementCreateView.as_view(),
        name="announcement_create",
    ),
    path(
        "<int:pk>",
        views.AnnouncementDetailView.as_view(),
        name="announcement_detail",
    ),
    path(
        "update/<int:pk>",
        views.AnnouncementUpdateView.as_view(),
        name="announcement_update",
    ),
    path(
        "delete/<int:pk>",
        views.AnnouncementDeleteView.as_view(),
        name="announcement_delete",
    ),
    path(
        "list/",
        views.AnnouncementListView.as_view(),
        name="announcement_list",
    ),
]

parking_urlpaterns = [
    path(
        "list/",
        views.ParkingListView.as_view(),
        name="parking_list",
    ),
]

urlpatterns = [
    path("visit/", include(visit_urlpatterns)),
    path("announcement/", include(announcement_urlpatterns)),
    path("parking/", include(parking_urlpaterns)),
]
