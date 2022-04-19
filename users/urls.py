# django
# from django.urls import path

# django
from django.urls import path

from . import views as users_views

urlpatterns = [
    path(
        "login/",
        users_views.LoginView.as_view(),
        name="login",
    ),
    path(
        "register/",
        users_views.UserCreateView.as_view(),
        name="register",
    ),
]
