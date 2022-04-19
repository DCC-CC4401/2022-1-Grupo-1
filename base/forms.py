# django
from django.forms import ModelForm


class BaseModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            attrs = field.widget.attrs
            if "class" not in attrs:
                attrs["class"] = ""

            attrs["class"] = "form-control "
