from schema import And, Optional


class RobotSchema:

    create = {
        "name": And(str),
        "description": And(str),
        "rosbridge_url": And(str),
    }

    update = {
        "name": And(str),
        "subscribed_numbers": And(list),
        "rosbridge_url": And(str),
        "owner_id": And(int)
    }