"""
# 1. Load and Explore the Dataset
import json

# Load the dataset
with open('data.json', 'r') as file:
    data = json.load(file)

# Inspect intents
intents = data['intents']
print(f"Number of intents: {len(intents)}")
for intent in intents[:5]:  # Display a few intents
    print(f"Tag: {intent['tag']}, Patterns: {intent['patterns']}, Responses: {intent['responses']}")

2. Preprocess Data
Convert the patterns into numerical representations for training a model.

import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Extract data
patterns = []
tags = []
responses = {}

for intent in intents:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        tags.append(intent['tag'])
    responses[intent['tag']] = intent['responses']

# Encode tags
label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(tags)

# Tokenize patterns
tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(patterns)
word_index = tokenizer.word_index

# Convert patterns to sequences
sequences = tokenizer.texts_to_sequences(patterns)
padded_sequences = pad_sequences(sequences, padding='post')

# Check shapes
print(f"Vocabulary Size: {len(word_index)}")
print(f"Number of samples: {len(padded_sequences)}")


3. Train-Test Split
Split the data into training and testing sets.

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    padded_sequences, labels, test_size=0.2, random_state=42)

print(f"Training samples: {len(X_train)}, Testing samples: {len(X_test)}")


4. Build and Train the Model
Use a simple neural network to classify user inputs into tags.

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

# Model configuration
vocab_size = len(word_index) + 1
embedding_dim = 16
max_length = padded_sequences.shape[1]

# Build the model
model = Sequential([
    Embedding(vocab_size, embedding_dim, input_length=max_length),
    LSTM(32, return_sequences=True),
    Dropout(0.2),
    LSTM(32),
    Dense(32, activation='relu'),
    Dense(len(label_encoder.classes_), activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test))


5. Evaluate the Model
Check the model's performance on the test set.

loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")


6. Save and Load the Model
Save the trained model and other necessary components for deployment.

# Save the model
model.save("chatbot_model.h5")

# Save tokenizer and label encoder
import pickle
with open('tokenizer.pkl', 'wb') as handle:
    pickle.dump(tokenizer, handle)
with open('label_encoder.pkl', 'wb') as handle:
    pickle.dump(label_encoder, handle)

7. Inference
Create a function to predict and generate responses.

def predict_response(user_input):
    # Preprocess input
    seq = tokenizer.texts_to_sequences([user_input])
    padded_seq = pad_sequences(seq, maxlen=max_length, padding='post')

    # Predict
    prediction = model.predict(padded_seq)
    tag = label_encoder.inverse_transform([np.argmax(prediction)])[0]

    # Generate response
    return np.random.choice(responses[tag])

# Test the chatbot
print(predict_response("Hi there!"))


"""