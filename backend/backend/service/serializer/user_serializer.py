from django.contrib.auth.models import User as UserEntity

"""
Serialize the given user to a JSON string.
"""
def to_json(user: UserEntity) -> str:
    return ("{\"username\":" +  f"\"{user.username}\",\n" +
            "\"email\":" +  f"\"{user.email}\",\n" +
            "\"password\":" +  f"\"{user.password}\",\n" +
            "\"first_name\":" +  f"\"{user.first_name}\",\n" +
            "\"last_name\":" +  f"\"{user.last_name}\"" + "}")