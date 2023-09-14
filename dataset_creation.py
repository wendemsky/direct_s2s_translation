import os
import csv

# Paths to audio folders
english_audio_folder = 'english_audio'
korean_audio_folder = 'korean_audio'
english_text_file = 'english_text.txt'
korean_text_file = 'korean_text.txt'

# Read the English and Korean text files
with open(english_text_file, 'r', encoding='utf-8') as eng_file, \
     open(korean_text_file, 'r', encoding='utf-8') as kor_file:
    english_translations = eng_file.readlines()
    korean_translations = kor_file.readlines()

# Ensure the audio and text lists match
if len(english_translations) != len(korean_translations):
    raise ValueError("Number of audio files and translations don't match!")

# Create a list to hold dataset entries
dataset = []

# Walk through the English audio folder
for root, _, files in os.walk(english_audio_folder):
    for file in files:
        if file.endswith('.mp3'):
            # Create the file paths for English and Korean audio
            english_audio_path = os.path.join(root, file)
            korean_audio_path = os.path.join(korean_audio_folder, file)

            # Get the corresponding translations
            index = int(file.split('.')[0]) - 1
            english_translation = english_translations[index].strip()
            korean_translation = korean_translations[index].strip()

            dataset.append([english_audio_path, english_translation, korean_audio_path, korean_translation])

# Save the dataset to a CSV file
with open('speech_to_speech_dataset.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['audio_path_english', 'translation_english', 'audio_path_korean', 'translation_korean'])
    csv_writer.writerows(dataset)
