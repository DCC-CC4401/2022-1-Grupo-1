# django
from django.urls import include
from django.urls import path

from . import views

visit_urlpatterns = [
    path("create/", views.VisitCreateView.as_view(), name="visit_create"),
]

urlpatterns = [
    path("visit/", include(visit_urlpatterns)),
]
