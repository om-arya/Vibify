from django.http import HttpResponse
from http import HTTPStatus
from django.core.exceptions import ObjectDoesNotExist
from backend.models import UserEntity
from backend.service.serializer import user_serializer

# https://docs.djangoproject.com/en/5.1/topics/auth/default/#topic-authorization

"""
Insert a user with the given fields into the database.

The given username and email address must not be in use,
or an error is returned.
"""
def create_user(username: str, email: str, password: str, first_name: str, last_name: str) -> HttpResponse:
    try:
        if UserEntity.objects.filter(username=username).exists():
            return HttpResponse(f"The username '{username}' is taken", status=HTTPStatus.CONFLICT)
        
        if UserEntity.objects.filter(email=email).exists():
            return HttpResponse(f"The email address '{email}' is in use", status=HTTPStatus.CONFLICT)
    except Exception as e:
        return HttpResponse(f"Caught exception: {e}", status=HTTPStatus.INTERNAL_SERVER_ERROR)

    UserEntity.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

    return HttpResponse(f"User '{username}' created successfully", status=HTTPStatus.CREATED)

"""
Return the user if the given username and password are
valid credentials. Otherwise, return an error.
"""
def authenticate_user_by_username(username: str, password: str) -> HttpResponse:
    try:
        user = UserEntity.objects.authenticate(username=username, password=password)
    except ObjectDoesNotExist:
        return HttpResponse(f"User with username '{username}' does not exist", status=HTTPStatus.NOT_FOUND)
    except Exception as e:
        return HttpResponse(f"Caught exception: {e}", status=HTTPStatus.INTERNAL_SERVER_ERROR)
    
    if user:
        user_json = user_serializer.to_json(user)
        return HttpResponse(user_json, content_type="application/json", status=HTTPStatus.OK)
    else:
        return HttpResponse("Credentials are invalid", status=HTTPStatus.UNAUTHORIZED)

"""
Return the user if the given email and password are
valid credentials. Otherwise, return an error.
"""
def authenticate_user_by_email(email: str, password: str) -> HttpResponse:
    try:
        user = UserEntity.objects.authenticate(email=email, password=password)
    except ObjectDoesNotExist:
        return HttpResponse(f"User with email '{email}' does not exist", status=HTTPStatus.NOT_FOUND)
    except Exception as e:
        return HttpResponse(f"Caught exception: {e}", status=HTTPStatus.INTERNAL_SERVER_ERROR)
    
    if user:
        user_json = user_serializer.to_json(user)
        return HttpResponse(user_json, content_type="application/json", status=HTTPStatus.OK)
    else:
        return HttpResponse("Credentials are invalid", status=HTTPStatus.UNAUTHORIZED)
    
"""
Update the email address of the user with the given
username.

If the user is not found, return an error.
"""
def set_user_email(username: str, new_email: str) -> HttpResponse:
    try:
        user = UserEntity.objects.get(username=username)
        user.email = new_email
        user.save()
        return HttpResponse(f"User '{username}' email address changed to '{new_email}' successfully", status=HTTPStatus.OK)
    except ObjectDoesNotExist:
        return HttpResponse(f"User '{username}' not found", status=HTTPStatus.NOT_FOUND)
    except Exception as e:
        return HttpResponse(f"Caught exception: {e}", status=HTTPStatus.INTERNAL_SERVER_ERROR)

"""
Update the password of the user with the given username.

If the user is not found, return an error.
"""
def set_user_password(username: str, new_password: str) -> HttpResponse:
    try:
        user = UserEntity.objects.get(username=username)
        user.set_password(new_password)
        user.save()
        return HttpResponse(f"User '{username}' password changed successfully", status=HTTPStatus.OK)
    except ObjectDoesNotExist:
        return HttpResponse(f"User '{username}' not found", status=HTTPStatus.NOT_FOUND)
    except Exception as e:
        return HttpResponse(f"Caught exception: {e}", status=HTTPStatus.INTERNAL_SERVER_ERROR)
    
"""
Update the first name of the user with the given
username.

If the user is not found, return an error.
"""
def set_user_first_name(username: str, new_first_name: str) -> HttpResponse:
    try:
        user = UserEntity.objects.get(username=username)
        user.first_name = new_first_name
        user.save()
        return HttpResponse(f"User '{username}' first name changed to '{new_first_name}' successfully", status=HTTPStatus.OK)
    except ObjectDoesNotExist:
        return HttpResponse(f"User '{username}' not found", status=HTTPStatus.NOT_FOUND)
    except Exception as e:
        return HttpResponse(f"Caught exception: {e}", status=HTTPStatus.INTERNAL_SERVER_ERROR)

"""
Update the last name of the user with the given
username.

If the user is not found, return an error.
"""
def set_user_last_name(username: str, new_last_name: str) -> HttpResponse:
    try:
        user = UserEntity.objects.get(username=username)
        user.last_name = new_last_name
        user.save()
        return HttpResponse(f"User '{username}' last name changed to '{new_last_name}' successfully", status=HTTPStatus.OK)
    except ObjectDoesNotExist:
        return HttpResponse(f"User '{username}' not found", status=HTTPStatus.NOT_FOUND)
    except Exception as e:
        return HttpResponse(f"Caught exception: {e}", status=HTTPStatus.INTERNAL_SERVER_ERROR)

"""
Delete the user with the given username.

If the user is not found, return an error.
"""
def delete_user(username: str) -> HttpResponse:
    try:
        user = UserEntity.objects.get(username=username)
        user.delete()
        return HttpResponse(f"User '{username}' deleted successfully", status=HTTPStatus.OK)
    except ObjectDoesNotExist:
        return HttpResponse(f"User '{username}' not found", status=HTTPStatus.NOT_FOUND)
    except Exception as e:
        return HttpResponse(f"Caught exception: {e}", status=HTTPStatus.INTERNAL_SERVER_ERROR)