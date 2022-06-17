# django
from django.urls import reverse

from base.views import BaseCreateView
from base.views import BaseDeleteView
from base.views import BaseDetailView
from base.views import BaseListView
from base.views import BaseUpdateView
from department.models import Parking


class ParkingListView(BaseListView):
    title = "Estacionamientos"
    model = Parking
    login_required = True
    permission_required = ()
    template_name = "parking/list.html"
    