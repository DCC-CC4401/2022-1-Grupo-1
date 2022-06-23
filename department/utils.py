# standard library
import random
import string

# django
from django.apps import apps


def create_validation_code():
    ValidationCode = apps.get_model("department", "ValidationCode")
    code = ""
    length = 10
    choices = string.ascii_letters + string.digits
    while True:
        code = "".join(random.choices(choices, k=length))
        if not ValidationCode.objects.filter(code=code).exists():
            break
    return code
