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

    if "index" not in event:
        valid["message"] = "Structure of event is incorrect"
        return valid

    valid["index"] = int(event["index"])

    if not isinstance(valid["index"],int):
        valid["message"] = "Not a integer."
        return valid

    if valid["index"] < 0:
        valid["message"] = "Index is not positive"
        return valid
    
    valid["state"] = True
    return valid


def function(event, context):

    logger.info('Event: %s', event)
    
    event = event["queryStringParameters"]
    
    valid = validate_event(event)    

    if valid["state"] == False:
        return make_response(valid, 400)

    index = valid['index']

    f = float(findIndex(index))

    logger.info('Fibonaci Response : %s', event)

    response = {}
    response["index"] = index
    response["response"] = f
    response["state"] = True

    return make_response(response, 200)

