# django
from django.urls import include
from django.urls import path

from . import views

visit_urlpatterns = [
    path("create/", views.VisitCreateView.as_view(), name="visit_create"),
]

announcement_urlpatterns = [
    path("create/", views.AnnouncementCreateView.as_view(), name="announcement_create"),
    path("list/", views.AnnouncementListView.as_view(), name="announcement_create"),
]

urlpatterns = [
    path("visit/", include(visit_urlpatterns)),
    path("announcement/", include(announcement_urlpatterns)),
]
