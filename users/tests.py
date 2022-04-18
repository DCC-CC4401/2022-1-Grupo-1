# django
from django.test import TestCase

from .models import User


class UserTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            rut="11.111.111-1",
            email="johndoe@example.com",
            name="John",
            first_last_name="asd",
            second_last_name="das",
            phone="+569988761234",
        )

    def test_lower_case_emails(self):
        """
        Tests that users are created with lower case emails
        """
        # local part is case-sensitive
        self.user.email = "Hello@example.com"
        self.user.save()
        self.assertEqual(self.user.email, "Hello@example.com")

        # domain part is case-insesitive
        self.user.email = "hello@ExamPle.com"
        self.user.save()
        self.assertEqual(self.user.email, "hello@example.com")
