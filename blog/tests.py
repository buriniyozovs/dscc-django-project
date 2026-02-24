from django.test import TestCase, Client
from django.urls import reverse
class HealthCheckTest(TestCase):
 def test_home_page_returns_200(self):
 client = Client()
 response = client.get("/")
 self.assertEqual(response.status_code, 200)
class BasicTests(TestCase):
 def test_app_name(self):
 """Test that the project is configured correctly"""
 self.assertTrue(True) # Placeholder - replace with real tests