from django.http import HttpResponse
from http import HTTPStatus
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User as UserEntity
from backend.models import VibeEntity
from backend.service.serializer import vibe_serializer
from django.core.serializers import serialize
from django.db import transaction

from backend.vibe_parametrization.vibe_parametrizer import assign_music_parameters
from backend.song_selection.song_selector import get_playlist

# https://docs.djangoproject.com/en/5.1/topics/db/queries/
# https://docs.djangoproject.com/en/5.1/topics/db/queries/#field-lookups

# TODO: Use Memcached for this
song_cache = {} # vibe ID : song list

"""
Insert a vibe into the database with the given name and color,
belonging to the user with the given username. The name is used
as a prompt to assign parameters, then initialize and cache a
new playlist.

The vibe's name must be unique for the user; an error is returned
otherwise.
"""
def create_vibe(username: str, name: str, color: str) -> HttpResponse:
    try:
        user = UserEntity.objects.get(username=username)
        if VibeEntity.objects.filter(user=user, name=name).exists():
            return HttpResponse(f"Vibe with name '{name}' already exists for user '{username}'", status=HTTPStatus.BAD_REQUEST)
    except ObjectDoesNotExist:
        return HttpResponse(f"User '{username}' not found", status=HTTPStatus.NOT_FOUND)
    except Exception as e:
        return HttpResponse(f"Caught exception: {e}", status=HTTPStatus.INTERNAL_SERVER_ERROR)
    
    d, e, v = assign_music_parameters(name)
    new_vibe = VibeEntity(name=name, color=color, danceability=d, energy=e, valence=v, user=user)

    try:
        new_vibe.save()
    except Exception as e:
        return HttpResponse(f"Caught exception: {e}", status=HTTPStatus.INTERNAL_SERVER_ERROR)

    new_playlist: list[str] = get_playlist(100, d, e, v)
    song_cache[new_vibe.id] = new_playlist

    return HttpResponse(f"Vibe created successfully with ID '{new_vibe.id}'", status=HTTPStatus.CREATED)

"""
Return the vibe with the given name that belongs to the given
user.

If the vibe is not found, return an error.
"""
def get_vibe(username: str, name: str) -> HttpResponse:
    try:
        vibe = VibeEntity.objects.get(user__username=username, name=name)
        vibe_json = vibe_serializer.to_json(vibe)
        return HttpResponse(vibe_json, status=HTTPStatus.OK)
    except ObjectDoesNotExist:
        return HttpResponse(f"Vibe with name '{name}' not found for user '{username}'", status=HTTPStatus.NOT_FOUND)
    except Exception as e:
        return HttpResponse(f"Caught exception: {e}", status=HTTPStatus.INTERNAL_SERVER_ERROR)

"""
Return all vibes belonging to the given user.
"""
def get_user_vibes(username: str) -> HttpResponse:
    try:
        user_vibes = VibeEntity.objects.filter(user__username=username)
        user_vibes_json = serialize('json', user_vibes)
        return HttpResponse(user_vibes_json, status=HTTPStatus.OK)
    except Exception as e:
        return HttpResponse(f"Caught exception: {e}", status=HTTPStatus.INTERNAL_SERVER_ERROR)

"""
Update the color of the vibe with the given name that
belongs to the given user.

If the vibe is not found, return an error.
"""
def set_vibe_color(username: str, name: str, new_color: str) -> HttpResponse:
    try:
        vibe = VibeEntity.objects.get(user__username=username, name=name)
        vibe.color = new_color
        vibe.save()
        return HttpResponse(f"Vibe with name '{name}' color changed to '{new_color}' successfully", status=HTTPStatus.OK)
    except ObjectDoesNotExist:
        return HttpResponse(f"Vibe with name '{name}' not found for user '{username}'", status=HTTPStatus.NOT_FOUND)
    except Exception as e:
        return HttpResponse(f"Caught exception: {e}", status=HTTPStatus.INTERNAL_SERVER_ERROR)

"""
Delete the vibe with the given name belonging to the given
user.

If the vibe is not found, return an error.
"""
def delete_vibe(username: str, name: str) -> HttpResponse:
    try:
        vibe = VibeEntity.objects.get(user__username=username, name=name)
        vibe.delete()
        return HttpResponse(f"Vibe with name '{name}' deleted successfully", status=HTTPStatus.OK)
    except ObjectDoesNotExist:
        return HttpResponse(f"Vibe with name '{name}' not found for user '{username}'", status=HTTPStatus.NOT_FOUND)
    except Exception as e:
        return HttpResponse(f"Caught exception: {e}", status=HTTPStatus.INTERNAL_SERVER_ERROR)