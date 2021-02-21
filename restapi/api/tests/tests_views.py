import json
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from django.http.request import HttpRequest
from django.contrib.auth.models import User

from api.models import PowerRequest, FibonaciRequest, FactorialRequest
from api.serializers import PowerSerializer, FibonaciSerializer, FactorialSerializer

from django.urls.exceptions import NoReverseMatch

from api.views import power_view, fibonaci_view, factorial_view

from rest_framework.test import force_authenticate
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

import uuid


class TestViews(TestCase):

    def setUp(self):

        name = str(uuid.uuid4())

        self.user = User.objects.create(
            username=name, email="test@gmail.com", password="test")
        self.token = Token.objects.get(user__username=name)

        self.client = APIClient()
        self.request = HttpRequest()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_ValidPowerRequest(self):

        response = self.client.get(
            reverse("get_power", kwargs={"base": -2.0, "exponent": 3}))
        o = PowerRequest(base=-2, exponent=3, response=-8)
        so = PowerSerializer(o)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, so.data)

    def test_InvalidUrlPower(self):

        with self.assertRaises(NoReverseMatch):
            self.client.get(
                reverse("get_power", kwargs={"base": "test", "exponent": 20}))

    def test_WrongMethodPower(self):

        response = self.client.post(
            reverse("get_power", kwargs={"base": 2, "exponent": 3}))

        self.assertEqual(response.status_code,  405)

    def test_ValidFibonaciRequest(self):

        response = self.client.get(
            reverse("get_fibonaci", kwargs={"index": 12}))

        f = FibonaciRequest(index=12, response=144)
        sf = FibonaciSerializer(f)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, sf.data)

    def test_InvalidParameterFibonaci(self):

        response = self.client.get(
            reverse("get_fibonaci", kwargs={"index": 0}))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.exception, True)

    def test_WrongMethodFibonaci(self):

        response = self.client.post(
            reverse("get_fibonaci", kwargs={"index": 2}))

        self.assertEqual(response.status_code,  405)

    def test_InvalidUrlFibonaci(self):

        with self.assertRaises(NoReverseMatch):
            self.client.get(reverse("get_fibonaci", kwargs={'index': "test"}))

        with self.assertRaises(NoReverseMatch):
            self.client.get(reverse("get_fibonaci", kwargs={'index': -1}))

    def test_ValidFactorialRequest(self):

        response = self.client.get(
            reverse("get_factorial", kwargs={"index": 12}))

        f = FactorialRequest(index=12, response=479001600)
        sf = FactorialSerializer(f)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, sf.data)

    def test_InvalidParameterFactorial(self):

        response = self.client.get(
            reverse("get_factorial", kwargs={"index": 0}))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.exception, True)

    def test_WrongMethodFactorial(self):

        response = self.client.post(
            reverse("get_factorial", kwargs={"index": 2}))

        self.assertEqual(response.status_code,  405)

    def test_InvalidUrlFactorial(self):

        with self.assertRaises(NoReverseMatch):
            self.client.get(reverse("get_factorial", kwargs={'index': "test"}))

        with self.assertRaises(NoReverseMatch):
            self.client.get(reverse("get_factorial", kwargs={'index': -1}))

    def tearDown(self):

        self.user.delete()
        self.client = None
        self.request = None
