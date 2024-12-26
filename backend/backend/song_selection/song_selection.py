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
Get a list of random song IDs close to the given danceability, energy,
and valence values (0.000 - 1.000).
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

# TESTS
    
import time
import statistics

length = 1
maximum, minimum = 0, float("inf")
max_dev, min_dev = None, None
all_elapsed = []
for d in range(1, 10):
    for e in range(1, 10):
        for v in range(1, 10):
            start = time.time()
            playlist = get_playlist(length, d / 10.0, e / 10.0, v / 10.0)
            end = time.time()

            elapsed = end - start
            all_elapsed.append(elapsed)
            print(f"Playlist (.{d}, .{e}, .{v}): {elapsed} seconds.")

            if elapsed > maximum:
                maximum = elapsed
                max_dev = (d, e, v)
            if elapsed < minimum:
                minimum = elapsed
                min_dev = (d, e, v)

print(f"Maximum: {maximum} seconds for {max_dev}.")
print(f"Minimum: {minimum} seconds for {min_dev}.")
print(f"Median: {statistics.median(all_elapsed)} seconds.")
print(f"Mean: {statistics.fmean(all_elapsed)} seconds.")
print(f"St. Deviation: {statistics.stdev(all_elapsed)} seconds.")