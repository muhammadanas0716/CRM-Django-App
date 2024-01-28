from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.
class LandingPageTest(TestCase):
    def test_status_code(self):
        #TODO: Some TEST
        response = self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)
        self.assertRaises(response.status_code, 404)
        pass

    def test_template_name(self):
        #TODO: Some TEST
        pass