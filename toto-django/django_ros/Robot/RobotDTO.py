from .RobotModel import Robot
from django_ros.User.UserDTO import UserDTO


class RobotDTO:

    @staticmethod
    def dict(robot: Robot) -> dict:
        if not robot.owner:
            owner = {}
        else:
            owner = UserDTO.dict(robot.owner)
        robot_dict = {
            'id': robot.id,
            'name': robot.name,
            'description': robot.description,
            'owner': owner,
            'rosbridge_url': robot.rosbridge_url
        }
        return robot_dict
