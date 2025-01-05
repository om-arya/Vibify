from backend.models import VibeEntity

"""
Serialize the given vibe to a JSON string with the fields
relevant to the client.
"""
def to_json(vibe: VibeEntity) -> str:
    return ("{\"name\":" +  f"\"{vibe.name}\",\n" +
            "\"color\":" +  f"\"{vibe.color}\"" + "}")