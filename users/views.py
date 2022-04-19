# django
from django.contrib.auth import views as auth_views
from django.views.generic import CreateView

from .forms import RegisterForm


class LoginView(auth_views.LoginView):
    """View to render login"""

    title = "Login"
    template_name = "registration/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context


class UserCreateView(CreateView):
    """View to create new users"""

    title = "Registro"
    template_name = "users/create.html"
    form_class = RegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context
