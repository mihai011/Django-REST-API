from power_lambda import function

from unittest import TestCase

import json
import math

class TestFibo(TestCase):

    def setUp(self):

        
        self.base = 12.23
        self.exponent = 23.23
        self.event = {"base":self.base, "exponent":self.exponent}

        self.response_test  = {}
        self.response_test["base"] = self.base
        self.response_test["exponent"] = self.exponent
        self.response_test["response"] = self.base ** self.exponent
        self.response_test["state"] = True
        self.response_test["status"] = 200


    def test_ValidEvent(self):

        event = json.dumps(self.event)

        response_valid = function(event, {})

        self.assertEqual(self.response_test, response_valid)

    def test_WrongEvent(self):

        event = "{test_wrong"
        del self.response_test
        self.response_test = {}
        self.response_test["status"] = 400
        self.response_test["state"] = False
        self.response_test["message"] = "Invalid event"

        response_valid = function(event, {})

        self.assertEqual(self.response_test, response_valid)


    def test_InvalidEventMissing(self):

        self.event = {"base":self.base}
        self.response_test["message"] = "Structure of event is incorrect."
        self.response_test["state"] = False
        self.response_test["status"] = 400
        del self.response_test["response"]
        del self.response_test["base"]
        del self.response_test["exponent"]

        event = json.dumps(self.event)

        response_valid = function(event, {})

        self.assertEqual(self.response_test, response_valid)


    def test_InvalidEventString(self):

        self.exponent = "test"
        self.event = {"base":self.base, "exponent":self.exponent}
        self.response_test["message"] = "Base and exponent need to be integers or floats."
        self.response_test["state"] = False
        self.response_test["status"] = 400
        self.response_test["exponent"] = self.exponent
        del self.response_test["response"]

        event = json.dumps(self.event)

        response_valid = function(event, {})

        self.assertEqual(self.response_test, response_valid)

    

    def tearDown(self):


        self.base = None
        self.base = None
        self.exponent = None
        self.event = None

        self.response_test  = None
