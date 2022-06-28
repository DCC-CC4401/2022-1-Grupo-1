# django
from django.utils.translation import gettext_lazy as _

from base.views import BaseCreateView
from base.views import BaseListView
from department.forms import VisitForm
from department.models import Visit


class VisitCreateView(BaseCreateView):
    title = _("New visit")
    template_name = "visits/create.html"
    form_class = VisitForm
    login_required = True
    permission_required = ("department.add_visit",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["back_button"] = True
        return context


class VisitListView(BaseListView):
    model = Visit
    title = _("Visit List")
    template_name = "visits/list.html"
    login_required = True
    permission_required = ("department.view_visit",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_button"] = True
        return context
