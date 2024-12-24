import torch
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
from train_music_rec import MusicRecommender, VOCAB_SIZE, EMBED_DIM, HIDDEN_DIM, OUTPUT_DIM, dataset, text_pipeline

model = MusicRecommender(VOCAB_SIZE, EMBED_DIM, HIDDEN_DIM, OUTPUT_DIM)
checkpoint = torch.load('model.pth')
model.load_state_dict(checkpoint['model_state_dict'])
model.eval()

tokenizer = get_tokenizer('basic_english')
vocab = build_vocab_from_iterator(tokenizer(prompt) for prompt, _ in dataset)

prompt = "depressed"
prompt_indices = text_pipeline(prompt)
prompt_tensor = torch.tensor(prompt_indices, dtype=torch.int64).unsqueeze(0)

with torch.no_grad():
    predictions = model(prompt_tensor)

print(f"Predicted values for prompt '{prompt}':")
print(f"Danceability: {predictions[0][0].item()}")
print(f"Energy: {predictions[0][1].item()}")
print(f"Valence: {predictions[0][2].item()}")