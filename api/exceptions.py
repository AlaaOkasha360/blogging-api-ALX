from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        data = {
            "error": True,
            "status_code": response.status_code,
            "detail": response.data
        }
        return Response(data, status=response.status_code)
    return Response({"error": True, "detail": "Internal server error"}, status=500)
