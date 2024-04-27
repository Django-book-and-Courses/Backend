from datetime import datetime

class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Record the time when the request is received
        request.timestamp = datetime.now()

        # Continue processing the request
        response = self.get_response(request)

        return response
