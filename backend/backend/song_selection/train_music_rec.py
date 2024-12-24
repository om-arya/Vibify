import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
import pandas as pd

class MusicDataset(Dataset):
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        prompt = self.data.iloc[idx, 0]
        danceability = self.data.iloc[idx, 1]
        energy = self.data.iloc[idx, 2]
        valence = self.data.iloc[idx, 3]
        return prompt, torch.tensor([danceability, energy, valence], dtype=torch.float)

dataset = MusicDataset('music_prompts.csv')
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

tokenizer = get_tokenizer('basic_english')
vocab = build_vocab_from_iterator((tokenizer(prompt) for prompt, _ in dataset), specials=["<unk>"])
vocab.set_default_index(vocab["<unk>"])

def text_pipeline(text):
    return [vocab[token] for token in tokenizer(text)]

def collate_batch(batch):
    text_list, label_list = [], []
    for (_text, _label) in batch:
        text_list.append(torch.tensor(text_pipeline(_text), dtype=torch.int64))
        label_list.append(_label)
    return torch.nn.utils.rnn.pad_sequence(text_list, batch_first=True), torch.stack(label_list)

dataloader = DataLoader(dataset, batch_size=32, shuffle=True, collate_fn=collate_batch)

class MusicRecommender(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, output_dim, dropout=0):
        super(MusicRecommender, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.rnn = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.batch_norm = nn.BatchNorm1d(hidden_dim)
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, text):
        embedded = self.embedding(text)
        output, (hidden, cell) = self.rnn(embedded)
        hidden = hidden[-1]
        return self.fc(hidden)

VOCAB_SIZE = len(vocab)
EMBED_DIM = 200
HIDDEN_DIM = 128
OUTPUT_DIM = 3

model = MusicRecommender(VOCAB_SIZE, EMBED_DIM, HIDDEN_DIM, OUTPUT_DIM)

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

def save_checkpoint(state, filename='model.pth'):
    torch.save(state, filename)

def load_checkpoint(filename='model.pth'):
    checkpoint = torch.load(filename)
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    return checkpoint['epoch'], checkpoint['loss']

num_epochs = 500
start_epoch = 0

if __name__ == "__main__":
    try:
        start_epoch, loss = load_checkpoint()
        print(f"Resuming training from epoch {start_epoch+1}")
    except FileNotFoundError:
        print("No checkpoint found, starting training from scratch")

    model.train()
    losses = []
    for epoch in range(num_epochs):
        for batch in dataloader:
            text, labels = batch
            optimizer.zero_grad()
            predictions = model(text)
            loss = criterion(predictions, labels)
            loss.backward()
            optimizer.step()
        losses.append(loss.item())
        print(f'Epoch {epoch+1}, Loss: {round(loss.item(), 2)}')

        save_checkpoint({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'loss': loss,
        }, 'model.pth')

    print("Training complete.")
    losses.sort()
    print("Median loss: " + str(round(losses[num_epochs // 2], 2)))