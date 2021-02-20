import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from django.http.request import HttpRequest

from api.models import PowerRequest, FibonaciRequest, FactorialRequest
from api.serializers import PowerSerializer, FibonaciSerializer, FactorialSerializer

from django.urls.exceptions import NoReverseMatch

from api.views import power_view ,fibonaci_view, factorial_view

class TestPowerView(TestCase):

    def setUp(self):

        self.client = Client()
        self.request = HttpRequest()
        

    def test_ValidPowerRequest(self):

        response = self.client.get(
            reverse("get_power", kwargs={"base": -2.0, "exponent": 3}))
        o = PowerRequest(base=-2, exponent=3, response=-8)
        so = PowerSerializer(o)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, so.data)

    def test_InvalidUrl(self):

        with self.assertRaises(NoReverseMatch):
            self.client.get(
                reverse("get_power", kwargs={"base": "test", "exponent": 20}))

    def test_WrongMethod(self):

        response = self.client.post(
            reverse("get_power", kwargs={"base": 2, "exponent": 3}))

        self.assertEqual(response.status_code,  405)

    def test_RawView(self):

        self.request.method = "GET"
        response = power_view(self.request, "test", 10)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.exception, True)

    def tearDown(self):

        self.client = None
        self.request = None

class TestFibonaciView(TestCase):

    def setUp(self):

        self.client = Client()
        self.request = HttpRequest()

    def test_ValidFibonaciRequest(self):

        response = self.client.get(
            reverse("get_fibonaci", kwargs={"index": 12}))

        f = FibonaciRequest(index=12, response=144)
        sf = FibonaciSerializer(f)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, sf.data)

    def test_InvalidParameter(self):

        response = self.client.get(
            reverse("get_fibonaci", kwargs={"index": 0}))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.exception, True)

    def test_WrongMethod(self):

        response = self.client.post(
            reverse("get_fibonaci", kwargs={"index":2}))

        self.assertEqual(response.status_code,  405)

    def test_InvalidUrl(self):

        with self.assertRaises(NoReverseMatch):
            self.client.get(reverse("get_fibonaci", kwargs={'index': "test"}))

        with self.assertRaises(NoReverseMatch):
            self.client.get(reverse("get_fibonaci", kwargs={'index': -1}))

    def test_RawView(self):

        self.request.method = "GET"
        response = fibonaci_view(self.request, "test")

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.exception, True)

    def tearDown(self):

        self.client = None
        self.request = None


class TestFactorialView(TestCase):

    def setUp(self):

        self.client = Client()
        self.request = HttpRequest()

    def test_ValidFactorialRequest(self):

        response = self.client.get(
            reverse("get_factorial", kwargs={"index": 12}))

        f = FactorialRequest(index=12, response=479001600)
        sf = FactorialSerializer(f)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, sf.data)

    def test_InvalidParameter(self):

        response = self.client.get(
            reverse("get_factorial", kwargs={"index": 0}))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.exception, True)

    def test_WrongMethod(self):

        response = self.client.post(
            reverse("get_factorial", kwargs={"index":2}))

        self.assertEqual(response.status_code,  405)

    def test_InvalidUrl(self):

        with self.assertRaises(NoReverseMatch):
            self.client.get(reverse("get_factorial", kwargs={'index': "test"}))

        with self.assertRaises(NoReverseMatch):
            self.client.get(reverse("get_factorial", kwargs={'index': -1}))

    def test_RawView(self):

        self.request.method = "GET"
        response = factorial_view(self.request, "test")

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.exception, True)

    def tearDown(self):

        self.client = None
        self.request = None