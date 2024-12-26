import pandas as pd

# TODO: Initialize these in a separate file and import
song_data = './song_data.csv'

all_songs = pd.read_csv(song_data)['track_id'].tolist()
all_popularities = pd.read_csv(song_data)['popularity'].tolist()

all_danceabilities = pd.read_csv(song_data)['danceability'].tolist()
all_energies = pd.read_csv(song_data)['energy'].tolist()
all_valences = pd.read_csv(song_data)['valence'].tolist()

"""
Get a random song ID close to the given danceability, energy, and
valence values (0.000 - 1.000).

The threshold for "closeness" to the input values is increased
incrementally before re-looping through all available songs. There is no
maximum limit to the threshold (except for valence), so as to ensure that
the 'count' is met.

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
Get a list of random song IDs close to the given danceability, energy,
and valence values (0.000 - 1.000).
"""
def get_playlist(count: int, d: float, e: float, v: float) -> list[str]:
    playset: set[str] = set()
    threshold = .1
    while len(playset) < count:
        for i in range(len(all_songs)):
            if (all_songs[i] not in playset and abs(all_danceabilities[i] - d) < threshold
               and abs(all_energies[i] - e) < .6 * threshold and abs(all_valences[i] - v) < min(.3 * threshold, .25)
               and ((v >= .5 and all_valences[i] >= .5) or (v <= .5 and all_valences[i] <= .5))):
                    playset[all_songs[i]] = all_popularities[i]
            if len(playset) == count:
                break
        threshold *= 1.04
    return list(playset)

# TESTS
    
import time

total_start = time.time()

start1 = time.time()
playlist1 = get_playlist(.2, .3, .4, 1)
end1 = time.time()

start2 = time.time()
playlist2 = get_playlist(.1, .9, .1, 1)
end2 = time.time()

start3 = time.time()
playlist3 = get_playlist(.9, .1, .9, 1)
end3 = time.time()

start4 = time.time()
playlist4 = get_playlist(.9, .9, .1, 1)
end4 = time.time()

start5 = time.time()
playlist5 = get_playlist(.1, .1, .9, 1)
end5 = time.time()

start6 = time.time()
playlist6 = get_playlist(.1, .1, .1, 1)
end6 = time.time()

start7 = time.time()
playlist7 = get_playlist(.9, .9, .9, 1)
end7 = time.time()

start8 = time.time()
playlist8 = get_playlist(.9, .1, .1, 1)
end8 = time.time()

start9 = time.time()
playlist9 = get_playlist(.1, .9, .9, 1)
end9 = time.time()

start10 = time.time()
playlist10 = get_playlist(.5, .2, .6, 1)
end10 = time.time()

start11 = time.time()
playlist11 = get_playlist(.2, .3, .4, 1)
end11 = time.time()

start12 = time.time()
playlist12 = get_playlist(.1, .9, .1, 1)
end12 = time.time()

start13 = time.time()
playlist13 = get_playlist(.9, .1, .9, 1)
end13 = time.time()

start14 = time.time()
playlist14 = get_playlist(.9, .9, .1, 1)
end14 = time.time()

start15 = time.time()
playlist15 = get_playlist(.1, .1, .9, 1)
end15 = time.time()

start16 = time.time()
playlist16 = get_playlist(.1, .1, .1, 1)
end16 = time.time()

start17 = time.time()
playlist17 = get_playlist(.9, .9, .9, 1)
end17 = time.time()

start18 = time.time()
playlist18 = get_playlist(.9, .1, .1, 1)
end18 = time.time()

start19 = time.time()
playlist19 = get_playlist(.1, .9, .9, 1)
end19 = time.time()

start20 = time.time()
playlist20 = get_playlist(.5, .2, .6, 1)
end20 = time.time()

total_end = time.time()

print(f"Playlist 1 created in {end1 - start1} seconds.")
print(f"Playlist 2 created in {end2 - start2} seconds.")
print(f"Playlist 3 created in {end3 - start3} seconds.")
print(f"Playlist 4 created in {end4 - start4} seconds.")
print(f"Playlist 5 created in {end5 - start5} seconds.")
print(f"Playlist 6 created in {end6 - start6} seconds.")
print(f"Playlist 7 created in {end7 - start7} seconds.")
print(f"Playlist 8 created in {end8 - start8} seconds.")
print(f"Playlist 9 created in {end9 - start9} seconds.")
print(f"Playlist 10 created in {end10 - start10} seconds.")
print(f"Playlist 11 created in {end11 - start11} seconds.")
print(f"Playlist 12 created in {end12 - start12} seconds.")
print(f"Playlist 13 created in {end13 - start13} seconds.")
print(f"Playlist 14 created in {end14 - start14} seconds.")
print(f"Playlist 15 created in {end15 - start15} seconds.")
print(f"Playlist 16 created in {end16 - start16} seconds.")
print(f"Playlist 17 created in {end17 - start17} seconds.")
print(f"Playlist 18 created in {end18 - start18} seconds.")
print(f"Playlist 19 created in {end19 - start19} seconds.")
print(f"Playlist 20 created in {end20 - start20} seconds.")
print(f"TOTAL: {total_end - total_start} seconds.")