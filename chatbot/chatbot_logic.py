"""
import joblib
import os

# Load the trained model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_FILE = os.path.join(BASE_DIR, "models/chatbot_model.pkl")

with open(MODEL_FILE, "rb") as file:
  chatbot_model = joblib.load(file)

def chatbot_response(user_input):

  # Generate a chatbot response using the trained model.

  try:
    response = chatbot_model.predict([user_input])  # Assuming model has a `predict` method
    print(response)
    return response[0]  # Assuming it returns a list of responses
  except Exception as e:
    return f"Error: {str(e)}"

"""



import json
import os
import random
from .models import ChatMessage

# Load responses from the data.json file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "chatmodel/data.json")

def load_intents():
  # Load the chatbot intents from the JSON file.
  with open(DATA_FILE, "r") as file:
    return json.load(file)["intents"]

intents = load_intents()

def get_response(user_input, user_id):
  #Get a chatbot response based on user input.
  for intent in intents:
    for pattern in intent["patterns"]:
      if user_input.lower() in pattern.lower():
        # Save interaction in the database
        response = random.choice(intent["responses"])
        ChatMessage.objects.create(user_id= user_id, user_message=user_input, bot_response=response)
        return response
      
  # Default response if no match is found
  # return "I'm sorry, I didn't understand that. Can you rephrase?"

# Example usage
if __name__ == "__main__":
  print("Nasma Chatbot: your stress level is very high \nNasma Chatbot: How can I assist you today?")
  while True:
    user_message = input("You: ")
    if user_message.lower() in ["exit", "quit", "bye"]:
      print("Nasma Chatbot: Goodbye! Take care!")
      break
    response = get_response(user_message)
    print(f"Nasma Chatbot: {response}")
