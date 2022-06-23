from base.views import BaseListView
from base.views import BaseUpdateView
from department.forms import ParkingChangeForm
from department.models import Parking


class ParkingListView(BaseListView):
    title = "Estacionamientos"
    model = Parking
    login_required = True
    permission_required = ()
    template_name = "parking/list.html"


class ParkingUpdateView(BaseUpdateView):
    title = "Estacionamientos"
    model = Parking
    form_class = ParkingChangeForm
    login_required = True
    permission_required = ()
    template_name = "parking/update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["back_button"] = True
        return context

    def can_access(self, request):
        return self.object.user == request.user

    def get_title(self):
        return str(self.object)
