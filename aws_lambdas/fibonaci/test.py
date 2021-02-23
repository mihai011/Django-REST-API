from fibonaci_lambda import function

from unittest import TestCase

import json


class TestFibo(TestCase):


    def test_ValidEvent(self):

        event = {"index":12}

        response_test  = {}
        response_test["index"] = 12
        response_test["response"] = 144.0
        response_test["state"] = True
        response_test["status"] = 200

        event = json.dumps(event)

        response_valid = function(event, {})

        self.assertEqual(response_test, response_valid)

    def test_InvalidEventNegative(self):

        event = {"index":-12}

        response_test  = {}
        response_test["index"] = -12
        response_test["message"] = "Index is not positive"
        response_test["state"] = False
        response_test["status"] = 400

        event = json.dumps(event)

        response_valid = function(event, {})

        self.assertEqual(response_test, response_valid)

    def test_InvalidEventString(self):

        event = {"index":"test"}

        response_test  = {}
        response_test["index"] = "test"
        response_test["message"] = "Not a integer."
        response_test["state"] = False
        response_test["status"] = 400

        event = json.dumps(event)

        response_valid = function(event, {})

        self.assertEqual(response_test, response_valid)
    
    def test_InvalidEventFloat(self):

        event = {"index":23.34}

        response_test  = {}
        response_test["index"] = 23.34
        response_test["message"] = "Not a integer."
        response_test["state"] = False
        response_test["status"] = 400

        event = json.dumps(event)

        response_valid = function(event, {})

        self.assertEqual(response_test, response_valid)

            