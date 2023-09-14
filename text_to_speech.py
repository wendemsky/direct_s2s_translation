# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# Function to convert text to speech and save as mp3
def text_to_speech(input_file, language, output_folder):
    # Read the text from the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        sentences = file.readlines()

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert each sentence to audio
    for index, sentence in enumerate(sentences):
        sentence = sentence.strip()
        if sentence:
            # Create a gTTS object
            tts = gTTS(text=sentence, lang=language, slow=False)

            # Save the audio file
            audio_file = os.path.join(output_folder, f"{index+1}.mp3")
            tts.save(audio_file)

            print(f"Converted and saved: {audio_file}")

# Language for English and Korean
english_language = 'en'
korean_language = 'ko'

# Input and output folders
english_input_file = 'english_text.txt'
korean_input_file = 'korean_text.txt'
english_output_folder = 'english_audio'
korean_output_folder = 'korean_audio'

# Convert English text to audio
text_to_speech(english_input_file, english_language, english_output_folder)

# Convert Korean text to audio
text_to_speech(korean_input_file, korean_language, korean_output_folder)
