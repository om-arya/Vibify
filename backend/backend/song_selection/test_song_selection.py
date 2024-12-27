from song_selection import get_playlist, get_song
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