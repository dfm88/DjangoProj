from django.shortcuts import reverse
from django.test import TestCase

# Create your tests here.


class LandingPageTest(TestCase):

    # "test_" automatically recognized a a unit test
    def test_status_code(self):
        # self.client.(post, put, get...) : let us mocking the requests
        response = self.client.get(reverse("landing-page"))
        # Testing the response ASSERT EQUAL = 200
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        # Testing the used Template
        # self.client.(post, put, get...) : let us mocking the requests
        response = self.client.get(reverse("landing-page"))
        # Testing the used Template
        self.assertTemplateUsed(response, template_name="landing.html")
