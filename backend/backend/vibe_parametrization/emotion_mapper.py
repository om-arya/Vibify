from enum import Enum

class Correlation(Enum):
    STRONG_POS = 1
    MODERATE_POS = .5
    WEAK_POS = .2
    NO_EFFECT = 0
    WEAK_NEG = -.2
    MODERATE_NEG = -.5
    STRONG_NEG = -1

# Map each emotion to its correlation with danceability, energy,
# and valence.
emotion_map = {
    'admiration': ('WEAK_NEG', 'WEAK_POS', 'STRONG_POS'),
    'amusement': ('MODERATE_POS', 'NO_EFFECT', 'MODERATE_POS'),
    'anger': ('MODERATE_NEG', 'STRONG_POS', 'STRONG_NEG'),
    'annoyance': ('WEAK_NEG', 'MODERATE_POS', 'MODERATE_NEG'),
    'approval': ('WEAK_NEG', 'WEAK_NEG', 'MODERATE_POS'),
    'caring': ('MODERATE_NEG', 'WEAK_NEG', 'STRONG_POS'),
    'confusion': ('WEAK_POS', 'WEAK_NEG', 'WEAK_NEG'),
    'curiosity': ('WEAK_NEG', 'MODERATE_POS', 'WEAK_POS'),
    'desire': ('STRONG_POS', 'MODERATE_POS', 'MODERATE_POS'),
    'disappointment': ('STRONG_NEG', 'STRONG_NEG', 'MODERATE_NEG'),
    'disapproval': ('WEAK_NEG', 'MODERATE_NEG', 'MODERATE_NEG'),
    'disgust': ('WEAK_NEG', 'MODERATE_POS', 'STRONG_NEG'),
    'embarrassment': ('WEAK_NEG', 'MODERATE_NEG', 'MODERATE_NEG'),
    'excitement': ('STRONG_POS', 'STRONG_POS', 'STRONG_POS'),
    'fear': ('STRONG_POS', 'MODERATE_NEG', 'STRONG_NEG'),
    'gratitude': ('WEAK_NEG', 'MODERATE_NEG', 'STRONG_POS'),
    'grief': ('STRONG_NEG', 'STRONG_NEG', 'STRONG_NEG'),
    'joy': ('NO_EFFECT', 'WEAK_NEG', 'STRONG_POS'),
    'love': ('WEAK_POS', 'MODERATE_NEG', 'WEAK_POS'),
    'nervousness': ('WEAK_NEG', 'STRONG_POS', 'MODERATE_NEG'),
    'optimism': ('WEAK_POS', 'WEAK_NEG', 'MODERATE_POS'),
    'pride': ('MODERATE_POS', 'MODERATE_POS', 'STRONG_POS'),
    'realization': ('WEAK_NEG', 'NO_EFFECT', 'WEAK_POS'),
    'relief': ('WEAK_NEG', 'MODERATE_NEG', 'MODERATE_POS'),
    'remorse': ('STRONG_NEG', 'MODERATE_NEG', 'WEAK_NEG'),
    'sadness': ('STRONG_NEG', 'STRONG_NEG', 'STRONG_NEG'),
    'surprise': ('MODERATE_POS', 'STRONG_POS', 'WEAK_POS'),
    'neutral': ('NO_EFFECT', 'NO_EFFECT', 'NO_EFFECT'),
}