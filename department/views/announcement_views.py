# django
from django.urls import reverse

from base.views import BaseCreateView
from base.views import BaseDeleteView
from base.views import BaseDetailView
from base.views import BaseListView
from base.views import BaseUpdateView
from department.forms import AnnouncementChangeForm
from department.forms import AnnouncementForm
from department.models import Announcement


class AnnouncementCreateView(BaseCreateView):
    title = "Nuevo Anuncio"
    model = Announcement
    form_class = AnnouncementForm
    login_required = True
    permission_required = ("department.add_announcement",)
    template_name = "announcements/create.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.model(user=self.request.user)
        return kwargs


class AnnouncementUpdateView(BaseUpdateView):
    title = "Anuncios"
    model = Announcement
    form_class = AnnouncementChangeForm
    login_required = True
    permission_required = ("department.change_announcement",)
    template_name = "announcements/update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["back_button"] = True
        return context

    def can_access(self, request):
        return self.object.user == request.user

    def get_title(self):
        return str(self.object)


class AnnouncementDetailView(BaseDetailView):
    model = Announcement
    login_required = True
    permission_required = ("department.view_announcemnet",)
    context_object_name = "announcement"
    template_name = "announcements/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user == self.object.user:
            context["update_button"] = True
            context["delete_button"] = True
        return context

    def get_title(self):
        return str(self.object)


class AnnouncementDeleteView(BaseDeleteView):
    model = Announcement
    login_required = True
    permission_required = ("department.delete_announcement",)
    context_object_name = "announcement"
    template_name = "announcements/delete.html"

    def get_success_url(self):
        return reverse("announcement_list")

    def can_access(self, request):
        return self.object.user == request.user

    def get_title(self):
        return f"Eliminar {self.object}"


class AnnouncementListView(BaseListView):
    title = "Anuncios"
    model = Announcement
    login_required = True
    permission_required = ("department.view_announcement",)
    template_name = "announcements/list.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_button"] = True
        return context
