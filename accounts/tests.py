from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import CustomUser


# Create your tests here.
class SignupPageTest(TestCase):
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get("/accounts/signup", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testemail@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "testemail@email.com")

        __pycache__/
*.py[cod]
*$py.class
*.so
.venv
.venv2
db.sqlite3
.env
staticfiles/
