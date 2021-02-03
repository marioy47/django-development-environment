# config/test.py
from django.test import TestCase
from django.urls import reverse


class FirstTest(TestCase):
    def test_that_invalid_fails(self):
        """ This test fails on purpose """
        self.assertTrue(True)

    def test_that_testing_works(self):
        """ This test validates that the route /test-path/ is a valid path """
        res = self.client.get(reverse("test-path"))
        self.assertEqual(200, res.status_code)
