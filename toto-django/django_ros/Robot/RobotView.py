import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from django_ros.util import validate_body
from django_ros.LawnMower.LawnMowerSchema import RobotSchema
from .RobotController import RobotController


@csrf_exempt
@api_view(['POST'])
@validate_body(RobotSchema.create)
def create(request: Request) -> HttpResponse:
    body = request.data
    status, response_dict = RobotController.create(body['name'], \
                                    body['rosbridge_url'], body['owner_id'])
    response_json = json.dumps(response_dict, indent=4, separators=(',', ':'))
    return HttpResponse(response_json, content_type='application/json', status=status)


@csrf_exempt
@api_view(['GET'])
def read(request: Request) -> HttpResponse:
    status, response_dict = RobotController.read(request.user)
    response_json = json.dumps(response_dict, indent=4, separators=(',', ':'))
    return HttpResponse(response_json, content_type='application/json', status=status)


@csrf_exempt
@api_view(['POST'])
@validate_body(RobotSchema.update)
def update(request: Request) -> HttpResponse:
    body = request.data
    mower_id = body['id']
    name = body['name']
    description = body['description']
    rosbridge_url = body['rosbridge_url']
    owner_id = body['owner_id']
    status, response_dict = RobotController.update(mower_id, name, description, rosbridge_url, owner_id)
    response_json = json.dumps(response_dict, indent=4, separators=(',', ':'))
    return HttpResponse(response_json, content_type='application/json', status=status)


@csrf_exempt
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete(request: Request) -> HttpResponse:
    mower_id: str = request.query_params.get('mower_id')
    status, response_dict = RobotController.delete(mower_id)
    response_json = json.dumps(response_dict, indent=4, separators=(',', ':'))
    return HttpResponse(response_json, content_type='application/json', status=status)

