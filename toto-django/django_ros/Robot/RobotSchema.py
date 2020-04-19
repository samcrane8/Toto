from schema import And, Optional


class RobotSchema:

    create = {
        "name": And(str),
        "rosbridge_url": And(str),
        "owner_id": And(int)
    }

    update = {
        "id": And(str),
        "name": And(str),
        "subscribed_numbers": And(list),
        "rosbridge_url": And(str),
        "owner_id": And(int)
    }