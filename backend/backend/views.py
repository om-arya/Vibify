from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User as UserEntity
from model.vibe_entity import VibeEntity
from backend.backend.vibe_parametrization.vibe_parametrizer import assign_music_parameters
from backend.backend.song_selection.song_selector import get_playlist

# TODO: Store this in a real cache
song_cache = {} # vibe ID : song list

def create_vibe(request: HttpRequest, name: str, color: str, user: UserEntity):
    # TODO: Validate input

    d, e, v = assign_music_parameters(name)
    
    new_vibe = VibeEntity(name=name, color=color, danceability=d, energy=e, valence=v, user=user)
    new_vibe.save()

    new_playlist: list[str] = get_playlist(100, d, e, v)
    song_cache[new_vibe.id] = new_playlist

    return HttpResponse()