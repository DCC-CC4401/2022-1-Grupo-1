# django
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from .mixins import IndividualPermissionMixin
from .mixins import LoginPermissionRequiredMixin
from .mixins import TitleMixin


class BaseTemplateView(LoginPermissionRequiredMixin, TitleMixin, TemplateView):
    login_required = True
    permission_required = ()


class BaseDetailView(LoginPermissionRequiredMixin, TitleMixin, DetailView):
    login_required = True
    permission_required = ()


class BaseCreateView(LoginPermissionRequiredMixin, TitleMixin, CreateView):
    login_required = True
    permission_required = ()

    def get_title(self):
        if self.title:
            return self.title
        verbose_name = self.model._meta.verbose_name
        return f"{_('Create')} {verbose_name}"


class BaseUpdateView(
    IndividualPermissionMixin, LoginPermissionRequiredMixin, TitleMixin, UpdateView
):
    login_required = True
    permission_required = ()

    def get_title(self):
        if self.title:
            return self.title
        return f"{_('Update')} {self.object}"


class BaseListView(LoginPermissionRequiredMixin, TitleMixin, ListView):
    login_required = True
    permission_required = ()

    def get_title(self):
        if self.title:
            return self.title
        return self.model._meta.verbose_name_plural.title()


class BaseDeleteView(
    IndividualPermissionMixin, LoginPermissionRequiredMixin, TitleMixin, DeleteView
):
    login_required = True
    permission_required = ()

    def get_title(self):
        if self.title:
            return self.title
        verbose_name = self.model._meta.verbose_name
        return f"{_('Delete')}: {verbose_name}"


class IndexView(BaseTemplateView):
    title = "DepAssist"
    template_name = "base/index.html"
    login_required = False
    permission_required = ()
