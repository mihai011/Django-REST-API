import json
import math

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


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

    try:
        valid["index"] = int(event["index"])
    except ValueError as e:
        valid["message"] = "Not a integer."
        return valid

    if valid["index"] < 0:
        valid["message"] = "Index is not positive"
        return valid
    
    valid["state"] = True
    return valid


def function(event, context):
    
    event = event["queryStringParameters"]
    
    logger.info('Event: %s', event)
    
    valid = validate_event(event)    

    if valid["state"] == False:
        return make_response(valid, 400)

    index = valid['index']

    f = float(math.factorial(index))

    logger.info('Fibonaci Response : %s', event)

    response = {}
    response["index"] = index
    response["response"] = f
    response["state"] = True

    return make_response(response, 200)

