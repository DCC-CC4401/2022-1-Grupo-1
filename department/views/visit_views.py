from base.views import BaseCreateView
from department.forms import VisitForm


class VisitCreateView(BaseCreateView):
    title = "Nueva Visita"
    template_name = "visits/create.html"
    form_class = VisitForm
    login_required = True
    permission_required = ()
