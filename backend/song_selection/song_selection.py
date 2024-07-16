import pandas as pd
import random
import math

song_data = './song_data.csv'

all_songs = pd.read_csv(song_data)['track_id'].tolist()
all_popularities = pd.read_csv(song_data)['popularity'].tolist()

all_danceabilities = pd.read_csv(song_data)['danceability'].tolist()
all_energies = pd.read_csv(song_data)['energy'].tolist()
all_valences = pd.read_csv(song_data)['valence'].tolist()

"""
Get a list of random song IDs close to the given danceability, energy,
and valence values (0.000 - 1.000). The list is sorted in descending
order by popularity (0 - 100) so as to integrate with a triangular
random distribution function with a mode of 0, which will be more likely
to select the earlier (more popular) songs.

The threshold for "closeness" to the input values is increased
incrementally before re-looping through all available songs. There is no
maximum limit to the threshold (except for valence), so as to ensure that
the 'count' is met (this means close may not always be "close").

The closeness threshold is scaled down for energy, and scaled further
down for valence, as these values are considered more significant to
the characterization of a song. For the same reason, the closeness
threshold for valence has a maximum limit, and the valence of a selected
song must always be on the same side of the median as the input valence
(either both <= .5 or both >= .5).
"""
def make_playlist(d: float, e: float, v: float, count: int) -> list[str]:
    playlist_dict: dict[str, int] = {} # song ID : popularity
    threshold = .1
    while len(playlist_dict) < count:
        for i in range(len(all_songs)):
            if (all_songs[i] not in playlist_dict and abs(all_danceabilities[i] - d) < threshold
               and abs(all_energies[i] - e) < .6 * threshold and abs(all_valences[i] - v) < min(.3 * threshold, .25)
               and ((v >= .5 and all_valences[i] >= .5) or (v <= .5 and all_valences[i] <= .5))):
                    playlist_dict[all_songs[i]] = all_popularities[i]
            if len(playlist_dict) == count:
                break
        threshold *= 1.04
    return get_keylist_by_values_descending(playlist_dict)

def get_keylist_by_values_descending(dictionary: dict):
    sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

    keylist = []
    for key, _ in sorted_items:
        keylist.append(key)
    return keylist
    
"""
Get a list of random, distinct songs from the specified playlist. A
triangular distribution is used with a mode of 0 so that earlier songs
in the playlist are more likely to be selected.

'count' is automatically decreased to the length of the playlist if it
is too high, as there cannot be more distinct songs than songs in the
playlist.

The list, which is created from a set to prevent duplicates, is shuffled
so that if the same songs are returned from multiple calls, they will not
always be in the same relative order (since a set always hashes items in
the same order).
"""
def get_songs(playlist: list, count: int) -> set[str]:
    if count > len(playlist):
        count = len(playlist)

    songs = set()
    for _ in range(count):
        rand = math.floor(random.triangular(0, len(playlist), 0))
        while playlist[rand] in songs:
            rand = math.floor(random.triangular(0, len(playlist), 0))
        songs.add(playlist[rand])

    songs = list(songs)
    random.shuffle(songs)
    return songs

songs = get_songs(make_playlist(.2, .3, .4, 1000), 200)
print(songs)