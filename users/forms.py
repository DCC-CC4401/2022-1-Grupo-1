# django
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext as _

from department.enums import ValidationCodeStatus
from department.models import Department
from department.models import ValidationCode

from .enums import UserType
from .models import User


class RegisterForm(forms.ModelForm):
    user_type = forms.ChoiceField(
        label=_("User Type"),
        choices=UserType.CHOICES,
    )
    validation_code = forms.CharField(
        label=_("Validation Code"),
        required=False,
    )
    department_number = forms.IntegerField(
        label=_("Department"),
        required=False,
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput,
    )
    password_2 = forms.CharField(
        label=_("Confirm Password"),
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = [
            "user_type",
            "validation_code",
            "department_number",
            "rut",
            "email",
            "name",
            "first_last_name",
            "second_last_name",
            "phone",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            print(key, value.label)

    def clean_email(self):
        """
        Verify email is available.
        """
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError(_("An account with this email already exists"))
        return email

    def clean_password_2(self):
        """
        Verify both passwords match.
        """
        password = self.cleaned_data.get("password")
        password_2 = self.cleaned_data.get("password_2")
        if password is not None and password != password_2:
            raise forms.ValidationError(_("Your passwords must match"))
        return password_2

    def clean_department_number(self):
        department_number = self.cleaned_data["department_number"]
        if self.cleaned_data["user_type"] == UserType.HABITANT:
            if department_number is None:
                raise forms.ValidationError(_("You must specify a department number"))
            qs = Department.objects.filter(number=department_number)
            if not qs.exists():
                Department.objects.create(number=department_number)
            return department_number
        return None

    def clean_validation_code(self):
        validation_code = self.cleaned_data["validation_code"]
        if self.cleaned_data["user_type"] == UserType.DOORMAN:
            qs = ValidationCode.objects.filter(code=validation_code)
            if qs.exists() and qs[0].status == ValidationCodeStatus.AVAILABLE:
                return validation_code
            else:
                raise forms.ValidationError(_("The code entered isn't available"))
        return ""

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if self.cleaned_data["user_type"] == UserType.HABITANT:
            user.department = Department.objects.get(
                number=self.cleaned_data["department_number"]
            )
        if commit:
            user.save()
            if self.cleaned_data["user_type"] == UserType.DOORMAN:
                ValidationCode.objects.get(
                    code=self.cleaned_data["validation_code"]
                ).use(user)
        return user


class UserChangeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["readonly"] = True
        self.fields["department"].widget.attrs["readonly"] = True
        if self.fields["department"].initial is None:
            self.fields["department"].widget = forms.HiddenInput()

    class Meta:
        model = User
        fields = (
            "rut",
            "email",
            "name",
            "first_last_name",
            "second_last_name",
            "phone",
            "department",
        )


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """

    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "rut",
            "email",
            "name",
            "first_last_name",
            "second_last_name",
            "phone",
            "password",
            "password_2",
        ]

    def clean_password_2(self):
        """
        Verify both passwords match.
        """
        password = self.cleaned_data.get("password")
        password_2 = self.cleaned_data.get("password_2")
        if password is not None and password != password_2:
            raise forms.ValidationError("Your passwords must match")
        return password_2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = [
            "admin",
            "is_active",
            "rut",
            "email",
            "name",
            "first_last_name",
            "second_last_name",
            "phone",
            "password",
        ]

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
