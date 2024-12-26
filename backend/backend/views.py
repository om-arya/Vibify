from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User as UserEntity
from model.vibe_entity import VibeEntity
from song_selection.song_selection import get_playlist

# TODO: Store this in a real cache
song_cache = {} # vibe ID : song list

def create_vibe(request: HttpRequest, name: str, color: str, danceability: int, energy: int, valence: int, user: UserEntity):
    # TODO: Validate parameters

    new_vibe = VibeEntity(name=name, color=color, danceability=danceability, energy=energy, valence=valence, user=user)
    new_vibe.save()
    
    new_playlist: list[str] = get_playlist(100, danceability, energy, valence)
    song_cache[new_vibe.id] = new_playlist

    return HttpResponse()