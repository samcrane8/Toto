from django.contrib.auth.models import User
from .RobotModel import Robot
from django_ros.Robot.RobotDTO import RobotDTO
from .tasks import run_service


class RobotController:

    @staticmethod
    def create(name: str, owner_id: str, description: str, rosbridge_url: str) -> (int, dict):
        owner = User.objects.filter(id=owner_id).first()
        robot: Robot = Robot(name=name, owner=owner, description=description, rosbridge_url=rosbridge_url)
        robot.save()
        return 200, {'message': 'Successfully created Robot.'}

    @staticmethod
    def read() -> (int, list):
        return 200, [RobotDTO.dict(x) for x in Robot.objects.all()]

    @staticmethod
    def update(robot_id: str, name: str, description: str, rosbridge_url: str, owner_id: str) -> (int, dict):
        robot: Robot = Robot.objects.filter(id=robot_id).first()
        if not robot:
            return 400, {'message': 'No robot with this id exists.'}
        robot.name = name
        owner = User.objects.filter(id=owner_id).first()
        robot.owner = owner
        robot.description = description
        robot.rosbridge_url = rosbridge_url
        robot.save()
        return 200, {'message': 'Successfully patched Robot.'}

    @staticmethod
    def delete(mower_id: str):
        robot: Robot = Robot.objects.filter(id=mower_id).first()
        if not robot:
            return 400, {'message': 'No robot with this id exists.'}
        robot.delete()
        return 200, {'message': 'Robot successfully deleted.'}

    @staticmethod
    def run_service(robot_id: int, service_name: str, service_type: str):
        robot: Robot = Robot.objects.filter(id=robot_id).first()
        if not robot:
            return 400, {'message': 'No robot with this id exists.'}
        run_service.delay(robot_id, service_name, service_type)
        return 200, {'message': 'Robot service handed off to worker.'}
