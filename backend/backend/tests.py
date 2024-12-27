from music_recommender.music_recommender import assign_music_parameters
from song_selection.song_selection import get_playlist

result = assign_music_parameters("coding")
print(result)
playlist = get_playlist(100, result[0], result[1], result[2])
print(playlist)