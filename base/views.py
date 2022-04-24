# django
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView


class LoginPermissionRequiredMixin(PermissionRequiredMixin):
    """
    Verify that the user is authenticated (if required) and
    has the permission (if required)
    """

    login_required = None

    def get_login_required(self):
        if self.login_required is None:
            raise ImproperlyConfigured(
                "{0} is missing the login_required attribute. "
                "Define {0}.login_required, or override "
                "{0}.get_login_required().".format(self.__class__.__name__)
            )
        if isinstance(self.login_required, bool):
            return self.login_required
        else:
            raise ImproperlyConfigured(
                "{0} has improperly configure login_required_attribute. "
                "Define {0}.login_required as a bool or override"
                "{0}.get_login_required().".format(self.__class__.__name__)
            )

    def dispatch(self, request, *args, **kwargs):
        if self.get_login_required():
            if not request.user.is_authenticated:
                return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class TitleMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context

    def get_title(self):
        return self.title


class BaseTemplateView(LoginPermissionRequiredMixin, TitleMixin, TemplateView):
    login_required = True
    permission_required = ()


class BaseCreateView(LoginPermissionRequiredMixin, TitleMixin, CreateView):
    login_required = True
    permission_required = ()

    def get_title(self):
        if self.title:
            return self.title
        verbose_name = self.model._meta.verbose_name
        return f"Create {verbose_name}"


class BaseUpdateView(LoginPermissionRequiredMixin, TitleMixin, UpdateView):
    login_required = True
    permission_required = ()

    def get_title(self):
        if self.title:
            return self.title
        return f"Update {self.object}"


class BaseListView(LoginPermissionRequiredMixin, TitleMixin, ListView):
    login_required = True
    permission_required = ()

    def get_title(self):
        if self.title:
            return self.title
        return self.model._meta.verbose_name_plural.title()


class BaseDeleteView(LoginPermissionRequiredMixin, TitleMixin, DeleteView):
    login_required = True
    permission_required = ()

    def get_title(self):
        if self.title:
            return self.title
        verbose_name = self.model._meta.verbose_name
        return f"Delete {verbose_name}"


class IndexView(BaseTemplateView):
    title = "DepAssist"
    template_name = "base/index.html"
    login_required = False
    permission_required = ()
