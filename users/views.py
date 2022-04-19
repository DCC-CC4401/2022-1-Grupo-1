# django
from django.contrib.auth import views as auth_views


class LoginView(auth_views.LoginView):
    """View to render login"""

    title = "Login"
    template_name = "registration/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context
