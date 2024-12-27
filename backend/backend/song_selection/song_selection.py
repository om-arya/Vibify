from song_data import all_songs, all_danceabilities, all_energies, all_valences

"""
Get a random song ID close to the given danceability, energy, and
valence values (0.000 - 1.000).

The threshold for "closeness" to the input values is increased
incrementally before re-looping through all available songs. There is no
maximum limit to the threshold (except for valence), so as to ensure that
a song is found.

The closeness threshold is scaled down for energy, and scaled further
down for valence, as these values are considered more significant to
the characterization of a song. For the same reason, the closeness
threshold for valence has a maximum limit, and the valence of a selected
song must always be on the same side of the median as the input valence
(either both <= .5 or both >= .5).
"""
def get_song(d: float, e: float, v: float) -> str:
    threshold = .1
    while True:
        for i in range(len(all_songs)):
            if (abs(all_danceabilities[i] - d) < threshold and abs(all_energies[i] - e) < .6 * threshold
                and abs(all_valences[i] - v) < min(.3 * threshold, .25)
                and ((v >= .5 and all_valences[i] >= .5) or (v <= .5 and all_valences[i] <= .5))):
                return all_songs[i]
        threshold *= 1.04

"""
Get a list of random, unique song IDs close to the given danceability,
energy, and valence values (0.000 - 1.000).
"""
def get_playlist(length: int, d: float, e: float, v: float) -> list[str]:
    playset: set[str] = set()
    threshold = .1
    while len(playset) < length:
        for i in range(len(all_songs)):
            if (all_songs[i] not in playset and abs(all_danceabilities[i] - d) < threshold
               and abs(all_energies[i] - e) < .6 * threshold and abs(all_valences[i] - v) < min(.3 * threshold, .25)
               and ((v >= .5 and all_valences[i] >= .5) or (v <= .5 and all_valences[i] <= .5))):
                    playset.add(all_songs[i])
            if len(playset) == length:
                break
        threshold *= 1.04
    return list(playset)