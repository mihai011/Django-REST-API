from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.db import transaction
# Create your tests here.

from api.models import PowerRequest, FibonaciRequest, FactorialRequest

class TestPowerModel(TestCase):

    def test_ValidIntegers(self):

        p = PowerRequest(base=10, exponent=100)
        p.save()

        self.assertEqual(p.base, 10)
        self.assertEqual(p.exponent,  100)
        self.assertEqual(p.response, None)

    def test_ValidFloat(self):

        p = PowerRequest(base=10.12, exponent=23.12)
        p.save()

        self.assertEqual(p.base, 10.12)
        self.assertEqual(p.exponent, 23.12)
        self.assertEqual(p.response, None)

    def test_MissingFloatBase(self):

        with self.assertRaises(IntegrityError):
            p = PowerRequest(base=-12)
            p.save()

    def test_MissingFloatExponent(self):

        with self.assertRaises(IntegrityError):
            p = PowerRequest(exponent=-12)
            p.save()



class TestFibonaciModel(TestCase):

    def test_ValidInteger(self):

        f = FibonaciRequest(index=12345)
        f.save()

        self.assertEqual(f.index, 12345)

    def test_InvalidInteger(self):

        with self.assertRaises(IntegrityError):
            f = FibonaciRequest(index=-1)
            f.save()

        with self.assertRaises(ValidationError):
            f = FibonaciRequest(index=0)
            f.full_clean()

    def test_MissingInteger(self):

        with self.assertRaises(IntegrityError):
            f = FibonaciRequest()
            f.save()

        with self.assertRaises(ValidationError):
            f = FibonaciRequest()
            f.full_clean()


class TestFactorialModel(TestCase):

    def test_ValidInteger(self):

        f = FactorialRequest(index=12345)
        f.save()

        self.assertEqual(f.index, 12345)

    def test_InvalidInteger(self):

        with self.assertRaises(IntegrityError):
            f = FactorialRequest(index=-1)
            f.save()

        with self.assertRaises(ValidationError):
            f = FactorialRequest(index=0)
            f.full_clean()

    def test_MissingInteger(self):

        with self.assertRaises(IntegrityError):
            f = FactorialRequest()
            f.save()

        with self.assertRaises(ValidationError):
            f = FactorialRequest()
            f.full_clean()
    


    

    

        



