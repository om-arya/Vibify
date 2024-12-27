from vibe_parametrization.emotion_mapper import Correlation, emotion_map
from transformers import pipeline

# Text emotion classification model
# https://huggingface.co/SamLowe/roberta-base-go_emotions
classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

"""
This function assigns danceability, energy, and valence values
based on a given input.
"""
def assign_music_parameters(input: str):
    prompt = [f"I feel like \"{input}\" music"]
    model_outputs = classifier(prompt)[0]

    score_map = {}
    for item in model_outputs:
        score_map[item['label']] = item['score']
    
    d, e, v = .5, .5, .5
    for emotion in emotion_map:
        d_corr, e_corr, v_corr = emotion_map[emotion]
        d += Correlation[d_corr].value * score_map[emotion]
        e += Correlation[e_corr].value * score_map[emotion]
        v += Correlation[v_corr].value * score_map[emotion]
    d, e, v = min(max(d, .1), .9), min(max(e, .1), .9), min(max(v, .1), .9)
    return (d, e, v)