# django
# from django.urls import path

# django
from django.contrib.auth import views as auth_views
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
    path(
        "profile/",
        users_views.UserDetailView.as_view(),
        name="profile",
    ),
    path(
        "edit/",
        users_views.UserUpdateView.as_view(),
        name="user_edit",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
]
