import json
from schema import Schema, SchemaError
from django.http import HttpResponse


def validate_body(body_schema):
    def real_decorator(f):
        def wrapper(*args, **kwargs):
            request = args[0]
            try:
                if request.method == 'POST':
                    body = request.data
                    schema = Schema([body_schema])
                    schema.validate([body])
            except SchemaError as error:
                response_json = json.dumps({"message": str(error)}, indent=4, separators=(',', ':'))
                return HttpResponse(response_json, content_type="application/json", status=401)
            result = f(*args, **kwargs)
            return result
        return wrapper
    return real_decorator
