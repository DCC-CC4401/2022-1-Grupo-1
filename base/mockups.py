# standard library
import os
import random
import string
import uuid

from shutil import copyfile

# django
from django.conf import settings
from django.utils import timezone

from base.utils import random_phone
from base.utils import random_rut
from base.utils import random_string
from department.enums import ParkingStatus
from department.enums import ValidationCodeStatus
from department.models import Announcement
from department.models import Department
from department.models import Parking
from department.models import ValidationCode
from department.models import Visit
from users.models import User


class Mockup:
    def create_user(self, password=None, **kwargs):
        if kwargs.get("rut") is None:
            kwargs["rut"] = random_rut()

        if kwargs.get("email") is None:
            kwargs["email"] = "%s@gmail.com" % random_string(length=6)

        if kwargs.get("name") is None:
            kwargs["name"] = random_string(length=6)

        if kwargs.get("first_last_name") is None:
            kwargs["first_last_name"] = random_string(length=6)

        if kwargs.get("second_last_name") is None:
            kwargs["second_last_name"] = random_string(length=6)

        if kwargs.get("phone") is None:
            kwargs["phone"] = random_phone()

        user = User.objects.create(**kwargs)

        if password is not None:
            user.set_password(password)
            user.save()

        return user

    def create_validation_code(self, **kwargs):
        self.set_required_foreign_key(kwargs, "user", model="user")
        self.set_required_string(kwargs, "code")
        self.set_required_choice(kwargs, "status", ValidationCodeStatus.CHOICES)
        return ValidationCode.objects.create(**kwargs)

    def create_visit(self, **kwargs):
        self.set_required_foreign_key(kwargs, "department", model="department")
        self.set_required_rut(kwargs, "rut")
        self.set_required_string(kwargs, "name")
        self.set_required_string(kwargs, "first_last_name")
        self.set_required_string(kwargs, "second_last_name")
        self.set_required_phone(kwargs, "phone")
        self.set_required_date(kwargs, "date")
        self.set_required_time(kwargs, "check_in")
        return Visit.objects.create(**kwargs)

    def create_department(self, **kwargs):
        self.set_required_int(kwargs, "number", minimum=101, maximum=2001)
        return Department.objects.create(**kwargs)

    def create_announcement(self, **kwargs):
        self.set_required_foreign_key(kwargs, "user", model="user")
        self.set_required_date(kwargs, "date")
        self.set_required_string(kwargs, "title")
        self.set_required_string(kwargs, "description")
        self.set_required_file(kwargs, "image")
        return Announcement.objects.create(**kwargs)

    def create_parking(self, **kwargs):
        self.set_required_choice(kwargs, "status", ParkingStatus.CHOICES)
        self.set_required_int(kwargs, "number")
        if kwargs["status"] == ParkingStatus.OCCUPIED:
            self.set_required_foreign_key(kwargs, "department", model="department")
            self.set_required_license_plate(kwargs, "license_plate")
        return Parking.objects.create(**kwargs)

    def random_email(self):
        return "{}@{}.{}".format(
            random_string(length=6), random_string(length=6), random_string(length=2)
        )

    def random_int(self, minimum=-100000, maximum=100000):
        return random.randint(minimum, maximum)

    def random_uuid(self, *args, **kwargs):
        chars = string.digits
        return uuid.UUID("".join(random.choice(chars) for x in range(32)))

    def set_required_license_plate(self, data, field):
        if field not in data:
            license_plate = random_string(
                length=4, chars=string.ascii_uppercase, include_spaces=False
            ) + random_string(
                length=2,
                chars=string.digits,
                include_spaces=False,
            )
            data[field] = license_plate

    def set_required_phone(self, data, field, **kwargs):
        if field not in data:
            data[field] = random_phone()

    def set_required_boolean(self, data, field, default=None, **kwargs):
        if field not in data:

            if default is None:
                data[field] = not not random.randint(0, 1)
            else:
                data[field] = default

    def set_required_choice(self, data, field, choices, **kwargs):
        if field not in data:
            data[field] = random.choice(choices)[0]

    def set_required_date(self, data, field, **kwargs):
        if field not in data:
            data[field] = timezone.now().date()

    def set_required_time(self, data, field, **kwargs):
        if field not in data:
            data[field] = timezone.now().time()

    def set_required_datetime(self, data, field, **kwargs):
        if field not in data:
            data[field] = timezone.now()

    def set_required_email(self, data, field):
        if field not in data:
            data[field] = self.random_email()

    def set_required_file(self, data, field):
        if field in data:
            # do nothing if the field is in the data
            return

        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)

        if not os.path.exists(f"{settings.MEDIA_ROOT}test_files/"):
            os.makedirs(f"{settings.MEDIA_ROOT}test_files/")

        test_root = os.path.realpath(os.path.dirname(__file__))

        file_path = data.pop("{}_file_path".format(field), None)

        if file_path is None:
            file_path = "test_image.jpg"

        if not os.path.isfile(file_path):
            file_path = "{}/test_assets/{}".format(test_root, file_path)

        file_media_path = "test_files/{}".format(os.path.basename(file_path))
        final_path = "{}test_files/{}".format(
            settings.MEDIA_ROOT, os.path.basename(file_path)
        )

        copyfile(file_path, final_path)
        print(file_path)
        print(final_path)
        print(file_media_path)

        data[field] = file_media_path

    def set_required_foreign_key(self, data, field, model=None, **kwargs):
        if model is None:
            model = field

        if field not in data and "{}_id".format(field) not in data:
            data[field] = getattr(self, "create_{}".format(model))(**kwargs)

    def set_required_int(self, data, field, **kwargs):
        if field not in data:
            data[field] = self.random_int(**kwargs)

    def set_required_ip_address(self, data, field, **kwargs):
        if field not in data:
            ip = "{}.{}.{}.{}".format(
                self.random_int(minimum=1, maximum=255),
                self.random_int(minimum=1, maximum=255),
                self.random_int(minimum=1, maximum=255),
                self.random_int(minimum=1, maximum=255),
            )
            data[field] = ip

    def set_required_rut(self, data, field, minimum=1000000, maximum=99999999):
        if field not in data:
            data[field] = random_rut(minimum, maximum)

    def set_required_string(self, data, field, length=6, include_spaces=True):
        if field not in data:
            data[field] = random_string(
                length=length,
                include_spaces=include_spaces,
            )

    def set_required_url(self, data, field, length=6):
        if field not in data:
            data[field] = "http://{}.com".format(random_string(length=length))
