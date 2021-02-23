import json
import math

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def findIndex(n) : 
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

def make_response(data, status):

    response = {}

    for k, v in data.items():

        response[k] = v

    response["status"] = status
    
    return {"statusCode":status,
        "body":json.dumps(response)
    }
        
def validate_event(event):

    valid = {}
    valid["state"] = False
    if isinstance(event, str):
        try:
            event = json.loads(event)
        except Exception as e:
            logger.setLevel(logging.ERROR)
            logger.error("Not a valid json structure %s", event)
            valid["message"] = "Invalid event"
            return valid

    if "base" not in event or "exponent" not in event:
        valid["message"] = "Base and exponent need to be in query."
        return valid

    valid["base"] = float(event["base"])
    valid["exponent"] = float(event["exponent"])

    if type(valid["base"]) not in [int, float] or type(valid["exponent"]) not in [int, float]:
        valid["message"] = "Base and exponent need to be integers or floats."
        return valid

    
    valid["state"] = True
    return valid


def function(event, context):

    event = event["queryStringParameters"]

    logger.info('Event: %s', event)
    
    valid = validate_event(event)    

    if valid["state"] == False:
        return make_response(valid, 400)

    base = valid['base']
    exponent = valid["exponent"]
    p = base ** exponent

    logger.info('Fibonaci Response : %s', event)

    response = {}
    response["base"] = base
    response["exponent"] = exponent
    response["response"] = p
    response["state"] = True

    return make_response(response, 200)

