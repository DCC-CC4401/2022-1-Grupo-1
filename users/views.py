# django
from django.contrib.auth import views as auth_views
from django.utils.translation import gettext_lazy as _

from base.views import BaseCreateView
from base.views import BaseDetailView
from base.views import BaseUpdateView

from .forms import RegisterForm
from .forms import UserChangeForm


class LoginView(auth_views.LoginView):
    """View to render login"""

    title = _("Login")
    template_name = "registration/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context


class UserCreateView(BaseCreateView):
    """View to create new users"""

    title = _("Register")
    template_name = "users/create.html"
    form_class = RegisterForm
    login_required = False
    permission_required = ()


class UserDetailView(BaseDetailView):
    title = _("Profile")
    template_name = "users/detail.html"
    login_required = True
    permission_required = ()
    context_object_name = "user"

    def get_object(self):
        return self.request.user


class UserUpdateView(BaseUpdateView):
    title = _("Update profile")
    form_class = UserChangeForm
    template_name = "users/update.html"
    login_required = True
    permission_required = ()
    context_object_name = "user"

    def get_object(self):
        return self.request.user

    def can_access(self, request):
        return self.request.user == self.get_object()
