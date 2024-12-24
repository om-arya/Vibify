from django.db import models
from django.contrib.auth.models import User
from song_selection.song_selection import make_playlist, get_songs

class Vibe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    COLORS = {
        '#ff0000': 'red',
        '#008000': 'green',
        '#468499': 'blue',
    }

    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, choices=COLORS)
    danceability = models.IntegerField(min_value=0, max_value=9)
    energy = models.IntegerField(min_value=0, max_value=9)
    valence = models.IntegerField(min_value=0, max_value=9)

    class Meta:
        db_table = "vibes"
        ordering = ["name"]