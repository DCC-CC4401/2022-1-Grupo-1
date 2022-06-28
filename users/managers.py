# django
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(
        self, rut, email, name, first_last_name, second_last_name, phone, password=None
    ):
        if not rut:
            raise ValueError(_("Users must have a rut"))
        if not email:
            raise ValueError(_("Users must have an email address"))

        email = self.normalize_email(email)
        user = self.model(
            rut=rut,
            email=email,
            name=name,
            first_last_name=first_last_name,
            second_last_name=second_last_name,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, rut, email, name, first_last_name, second_last_name, phone, password=None
    ):
        user = self.model(
            rut=rut,
            email=self.normalize_email(email),
            name=name,
            first_last_name=first_last_name,
            second_last_name=second_last_name,
            phone=phone,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
