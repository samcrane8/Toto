from django.contrib.auth.models import User


class UserDTO:

    @staticmethod
    def dict(user: User) -> dict:
        user_dict = dict()
        user_dict['id'] = user.id
        user_dict['username'] = user.username
        user_dict['first_name'] = user.first_name
        user_dict['last_name'] = user.last_name
        user_dict['email'] = user.email
        return user_dict
