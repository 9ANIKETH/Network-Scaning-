import google.generativeai as genai
import os
import pyttsx3  # for voice output

# Simple speak function
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def aiProcess():
    API_KEY = "AIzaSyCjDMlLqH_TNE5AOLY85pFtviCHQM3S_JA"  # put your key here
    genai.configure(api_key=API_KEY)

    generation_config = {
        "temperature": 0.7,
        "top_p": 0.9,
        "top_k": 1,
        "max_output_tokens": 100,
    }

    try:
        model = genai.GenerativeModel(
            "models/gemini-2.5-pro", 
            generation_config=generation_config
        )
        convo = model.start_chat()

        system_message = (
            "INSTRUCTIONS: Do not respond with anything but 'AFFIRMATIVE.' "
            "SYSTEM MESSAGE: You are being used to power a voice assistant. "
            "As a voice assistant, use short sentences and direct answers."
        )
        convo.send_message(system_message)
        speak("System initialized. Ready for your command.")
        print("System initialized. Ready for your command.")

    except Exception as e:
        print(f"Error initializing Generative AI model: {e}")
        return

    stop_word = "exit"

    while True:
        user_input = input("Please enter your command or question: ").lower()

        if stop_word in user_input:
            speak("Stopping and exiting...")
            break

        convo.send_message(user_input)
        response = convo.last.text
        speak(response)
        print(f"AI: {response}")

    print("Exiting program...")
    os._exit(0)

# Start
aiProcess()
