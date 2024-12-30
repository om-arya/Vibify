from backend.music_recommendation.vibe_parametrization.emotion_mapper import Correlation, emotion_map
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
    model_output = classifier(prompt)[0]

    weight = {}
    for item in model_output:
        weight[item['label']] = item['score']
    
    d, e, v = .5, .5, .5
    for emotion in emotion_map:
        d_corr, e_corr, v_corr = emotion_map[emotion]
        d += Correlation[d_corr].value * weight[emotion]
        e += Correlation[e_corr].value * weight[emotion]
        v += Correlation[v_corr].value * weight[emotion]

    d, e, v = min(max(d, .1), .9), min(max(e, .1), .9), min(max(v, .1), .9)

    return (d, e, v)