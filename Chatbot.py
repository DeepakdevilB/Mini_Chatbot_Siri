"""
Project Title: Mini ChatBot  🧠🔊
Description: This is an AI-powered chatbot built using OpenAI's GPT-4o model. 
It allows real-time text-based conversation and also reads responses aloud using text-to-speech.
"""

from openai import OpenAI
import pyttsx3
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# --------------------- Configuration ---------------------
# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 190)  # Speech speed
engine.setProperty('volume', 1.0)  # Max volume
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

# Set your OpenAI API key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --------------------- Core Functions ---------------------
def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def chat_with_gpt(prompt):
    """Send a prompt to GPT and get a response."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    reply = response.choices[0].message.content.strip()
    return reply
   
# --------------------- Main Interaction ---------------------
print("\n\t\t 🤖 Welcome to the Student Companion Bot!\n")
user_name = input("Please enter your name: ")

if __name__ == "__main__":
    while True:
        user_input = input(f"{user_name} : ")
        if user_input.lower() in ["bye", "quit", "exit"]:
            goodbye = "Goodbye! Have a great day!"
            print("Siri :", goodbye)
            speak("BYE, have a good day . ")
            break

        response = chat_with_gpt(user_input)
        print("Siri :", response)
        speak(response)
