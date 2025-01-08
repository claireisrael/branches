from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class HomeTests(TestCase):
    def test_home_status_code(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Welcome to claire's Tech World!")