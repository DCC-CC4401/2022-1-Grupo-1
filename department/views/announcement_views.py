from base.views import BaseCreateView
from base.views import BaseListView
from department.forms import AnnouncementForm
from department.models import Announcement


class AnnouncementCreateView(BaseCreateView):
    title = "Nuevo Anuncio"
    model = Announcement
    form_class = AnnouncementForm
    login_required = True
    permission_required = ()
    template_name = "announcements/create.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context["form"].errors)
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.model(user=self.request.user)
        return kwargs


class AnnouncementListView(BaseListView):
    title = "Anuncios"
    model = Announcement
    login_required = True
    permission_required = ()
    template_name = "announcements/list.html"
    paginate_by = 12
