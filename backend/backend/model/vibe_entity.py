from django.db import models
from django.contrib.auth.models import User as UserEntity
from song_selection.song_selection import get_playlist, get_song

class VibeEntity(models.Model):
    class Meta:
        db_table = "vibes"
        ordering = ["name"]

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

    playlist: list[str] = []

    def initialize_playlist(self, count: int):
        self.playlist = get_playlist(count, self.danceability, self.energy, self.valence)

    def get_random_song(self):
        return get_song(self.danceability, self.energy, self.valence)