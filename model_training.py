import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Define the model architecture
latent_dim = 256  # Adjust this value as needed

# Define input layers
audio_input = Input(shape=(max_audio_length, 13))
text_input = Input(shape=(max_seq_length,))

# Define embedding layers for text data
# Use the same embedding layer for both source and target text
embedding_layer = Embedding(input_dim=len(english_tokenizer.word_index) + 1, output_dim=latent_dim)

text_embedding = embedding_layer(text_input)

# Define the encoder LSTM
encoder_lstm = LSTM(latent_dim, return_state=True)
encoder_outputs, state_h, state_c = encoder_lstm(audio_input)

# Connect encoder and decoder
decoder_lstm = LSTM(latent_dim, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(text_embedding, initial_state=[state_h, state_c])

# Define the output layer
output_layer = Dense(len(korean_tokenizer.word_index) + 1, activation='softmax')
output = output_layer(decoder_outputs)

# Define the model
model = Model([audio_input, text_input], output)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Print the model summary
model.summary()

# Prepare target sequences for training
Y_train = pad_sequences(Y_text, maxlen=max_seq_length, padding='post')
Y_train = to_categorical(Y_train, num_classes=len(korean_tokenizer.word_index) + 1)

# Train the model
model.fit([X_audio, X_text], Y_train, batch_size=64, epochs=50, validation_split=0.2)

# Save the trained model if needed
# model.save('speech_to_speech_translation_model.h5')
