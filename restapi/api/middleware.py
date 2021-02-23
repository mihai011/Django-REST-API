from .models import LogRequest
from .serializers import LogRequestSerializer

from .tasks import create_log
import json

class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

class LoggingMiddleware(BaseMiddleware):

    # for request
    def process_request(self, request):

        create_log.delay({"req":str(request)})
        
        return request

    def process_view(self, request, view_func, args, kwargs):

        j = {}
        j["path"] = request.path
        j["view"] = str(view_func)
        j["args"] = str(args)
        j["kwargs"] = str(args)
        s = create_log.delay(json.dumps(j))

    # for response
    def process_exception(self, exception):

        json = {"exception":str(exception)}
        create_log.delay(exception)
        
    
