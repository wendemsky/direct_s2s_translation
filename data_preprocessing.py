import os
import numpy as np
import librosa
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Paths to the audio folders and the CSV dataset file
english_audio_folder = 'english_audio'
korean_audio_folder = 'korean_audio'
dataset_file = 'speech_to_speech_dataset.csv'

# Load the dataset from the CSV file
dataset = pd.read_csv(dataset_file)

# Define the maximum sequence length for audio and text (adjust as needed)
max_audio_length = 100  # You can change this value based on your model's requirements
max_seq_length = 50  # Define your desired sequence length for text data

# Initialize lists to store audio features and text data
X_audio = []
X_text = []
Y_text = []

# Initialize tokenizers for text data
english_tokenizer = Tokenizer()
korean_tokenizer = Tokenizer()

# Extract MFCC features from audio and tokenize text
sample_rate = 22050  # Define the sample rate (adjust as needed)

# Function to plot MFCC features
def plot_mfcc(mfcc):
    plt.figure(figsize=(10, 4))
    plt.imshow(mfcc, cmap='viridis', origin='lower', aspect='auto')
    plt.title('MFCC Features')
    plt.xlabel('Time')
    plt.ylabel('MFCC Coefficients')
    plt.colorbar(format='%+2.0f dB')
    plt.show()

# Function to plot MFCC coefficients
def plot_mfcc_coefficients(mfcc):
    plt.figure(figsize=(8, 4))
    plt.plot(mfcc)
    plt.title('MFCC Coefficients')
    plt.xlabel('Frame')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()

for index, row in dataset.iterrows():
    # Load and preprocess audio
    audio_path = os.path.join(english_audio_folder, os.path.basename(row['audio_path_english']))
    signal, _ = librosa.load(audio_path, sr=sample_rate)
    mfccs = librosa.feature.mfcc(y=signal, sr=sample_rate, n_mfcc=13, hop_length=512, n_fft=2048)
    mfccs = pad_sequences([mfccs.T], maxlen=max_audio_length, padding='post')[0]  # Padding/truncating

    # Plot an example MFCC
    if index == 0:
        plot_mfcc(mfccs)
        # Print an example of MFCC coefficients for the first sample
        print("Example MFCC coefficients for the first sample:")
        print(mfccs)

    # Tokenize and encode English and Korean text
    english_text = row['translation_english']
    korean_text = row['translation_korean']
    english_seq = english_tokenizer.texts_to_sequences([english_text])[0]
    korean_seq = korean_tokenizer.texts_to_sequences([korean_text])[0]

    # Append to lists
    X_audio.append(mfccs)
    X_text.append(english_seq)  # Using English as input text
    Y_text.append(korean_seq)  # Using Korean as target text

# Convert lists to numpy arrays
X_audio = np.array(X_audio)
X_text = pad_sequences(X_text, maxlen=max_seq_length, padding='post')
Y_text = pad_sequences(Y_text, maxlen=max_seq_length, padding='post')

# Define the path for the new CSV file containing preprocessed data
preprocessed_csv_file = 'preprocessed_speech_to_speech_dataset.csv'

# Save the preprocessed data to the new CSV file
preprocessed_dataset = pd.DataFrame({'audio_path_english': dataset['audio_path_english'],
                                     'translation_english': dataset['translation_english'],
                                     'audio_path_korean': dataset['audio_path_korean'],
                                     'translation_korean': dataset['translation_korean'],
                                     'mfcc_features': list(X_audio),
                                     'english_sequence': X_text.tolist(),  # Convert to list
                                     'korean_sequence': Y_text.tolist()})  # Convert to list

preprocessed_dataset.to_csv(preprocessed_csv_file, index=False, encoding='utf-8')

print("Preprocessed dataset saved to:", preprocessed_csv_file)
