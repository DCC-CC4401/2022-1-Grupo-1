from base.views import BaseListView
from department.models import Parking


class ParkingListView(BaseListView):
    title = "Estacionamientos"
    model = Parking
    login_required = True
    permission_required = ()
    template_name = "parking/list.html"
