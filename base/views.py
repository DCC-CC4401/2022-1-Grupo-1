# django
from django.views.generic import TemplateView


class IndexView(TemplateView):

    title = "DepAssist"
    template_name = "base/index.html"
