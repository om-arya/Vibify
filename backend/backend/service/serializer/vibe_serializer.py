from backend.models import VibeEntity

"""
Serialize the given vibe to a JSON string.
"""
def to_json(vibe: VibeEntity) -> str:
    return ("{\"name\":" +  f"\"{vibe.name}\",\n" +
            "\"color\":" +  f"\"{vibe.color}\",\n" +
            "\"danceability\":" +  f"\"{vibe.danceability}\",\n" +
            "\"energy\":" +  f"\"{vibe.energy}\",\n" +
            "\"valence\":" +  f"\"{vibe.valence}\",\n" +
            "\"user\":" +  f"\"{vibe.user.username}\"" + "}")