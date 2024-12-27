from django.db import models
from django.contrib.auth.models import User as UserEntity
from backend.backend.song_selection.song_selector import get_playlist, get_song

class VibeEntity(models.Model):
    class Meta:
        db_table = "vibes"
        ordering = ["name"]

    playlist_length = 100

    COLORS = {
        '#ff0000': 'red',
        '#008000': 'green',
        '#468499': 'blue',
    }
    
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, choices=COLORS)
    danceability = models.FloatField()
    energy = models.FloatField()
    valence = models.FloatField()
    user = models.ForeignKey(UserEntity, on_delete=models.CASCADE)

    def get_random_song(self):
        return get_song(self.danceability, self.energy, self.valence)
    
    def initialize_playlist(self):
        self.playlist = get_playlist(self.playlist_length, self.danceability, self.energy, self.valence)

    def get_next_song(self):
        next = self.playlist.pop()
        if len(self.playlist == 0):
            self.initialize_playlist()
        return next
    