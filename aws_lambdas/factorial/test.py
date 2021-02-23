from factorial_lambda import function

from unittest import TestCase

import json
import math

class TestFibo(TestCase):

    def setUp(self):

        self.index = "12"
        self.event = {"index":self.index}

        self.res = {}
        self.res["index"] = int(self.index)
        self.res["response"] = float(math.factorial(int(self.index)))
        self.res["state"] = True
        self.res["status"] = 200
        
        self.response_test  = {}
        self.response_test["statusCode"] = 200
        self.response_test["body"] = json.dumps(self.res)

        self.bigger = {}
        self.bigger["queryStringParameters"] = self.event

        self.event = self.bigger

    def test_ValidEvent(self):

        response_valid = function(self.event, {})

        self.assertEqual(self.response_test, response_valid)

    def test_InvalidEventNegative(self):

        self.index = "-12"
        self.event = {"index":self.index}

        self.res = {}
        self.res["state"] = False
        self.res["index"] = int(self.index)
        self.res["message"] = "Index is not positive"
        self.res["status"] = 400
        
        self.response_test  = {}
        self.response_test["statusCode"] = 400
        self.response_test["body"] = json.dumps(self.res)

        self.bigger = {}
        self.bigger["queryStringParameters"] = self.event

        self.event = self.bigger

        response_valid = function(self.event, {})

        self.assertEqual(self.response_test, response_valid)

    def test_InvalidEventString(self):

        self.index = "test"
        self.event = {"index":self.index}

        self.res = {}
        self.res["state"] = False
        self.res["message"] = "Not a integer."
        self.res["status"] = 400
        
        self.response_test  = {}
        self.response_test["statusCode"] = 400
        self.response_test["body"] = json.dumps(self.res)

        self.bigger = {}
        self.bigger["queryStringParameters"] = self.event

        self.event = self.bigger

        response_valid = function(self.event, {})

        self.assertEqual(self.response_test, response_valid)
    
    def test_InvalidEventFloat(self):

        self.index = "12.23"
        self.event = {"index":self.index}

        self.res = {}
        self.res["state"] = False
        self.res["message"] = "Not a integer."
        self.res["status"] = 400
        
        self.response_test  = {}
        self.response_test["statusCode"] = 400
        self.response_test["body"] = json.dumps(self.res)

        self.bigger = {}
        self.bigger["queryStringParameters"] = self.event

        self.event = self.bigger

        response_valid = function(self.event, {})

        self.assertEqual(self.response_test, response_valid)
            