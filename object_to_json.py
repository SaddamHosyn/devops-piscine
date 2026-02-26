import json


class User:
    username = 'user'
    email = 'something@mail.com'


def create_new_user(data):
    try:
        parsed = json.loads(data)

        # Check if required keys exist
        if isinstance(parsed, dict) and "username" in parsed and "email" in parsed:
            user = User()
            user.username = parsed["username"]
            user.email = parsed["email"]
            return user

    except (json.JSONDecodeError, TypeError):
        pass

    # Return default user if invalid
    return User()


def user_to_json(user):
    # Only return JSON if user has custom attributes
    if user.__dict__:
        return json.dumps(user.__dict__)
    return json.dumps({})
