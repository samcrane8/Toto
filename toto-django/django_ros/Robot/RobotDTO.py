from .RobotModel import Robot
from django_ros.User.UserDTO import UserDTO


class RobotDTO:

    @staticmethod
    def dict(lawn_mower: Robot) -> dict:
        if not lawn_mower.owner:
            owner = {}
        else:
            owner = UserDTO.dict(lawn_mower.owner)
        lawn_mower_dict = {
            'id': str(lawn_mower.id),
            'name': lawn_mower.name,
            'phone_number': lawn_mower.phone_number,
            'subscribed_numbers': [],
            'owner': owner,
            'rosbridge_url': lawn_mower.rosbridge_url
        }
        return lawn_mower_dict
