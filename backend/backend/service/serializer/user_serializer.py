from backend.models import UserEntity

"""
Serialize the given user to a JSON string with the fields
relevant to the client.
"""
def to_json(user: UserEntity) -> str:
    return ("{\"username\":" +  f"\"{user.username}\",\n" +
            "\"email\":" +  f"\"{user.email}\",\n" +
            "\"first_name\":" +  f"\"{user.first_name}\",\n" +
            "\"last_name\":" +  f"\"{user.last_name}\"" + "}")