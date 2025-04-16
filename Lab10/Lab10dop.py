import requests
import pyttsx3
import webbrowser
import json
import pyaudio
from vosk import Model, KaldiRecognizer

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("voice", "english")  # Use English voice

model = Model("vosk-model-en-us-0.22-lgraph")  # English model
recognizer = KaldiRecognizer(model, 16000)
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def find_word(word):
    try:
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def process_command(command):
    if command.startswith("find "):
        word = command.split("find ")[1].strip()
        data = find_word(word)
        if data:
            meanings = data[0]["meanings"]
            speak(f"Found definitions for {word}.")
            return meanings
        else:
            speak("Sorry, no definitions found.")
            return None
    elif command == "save":
        if "meanings" in globals():
            with open("word_definitions.txt", "w") as f:
                json.dump(meanings, f, indent=2)
            speak("Definitions saved to file.")
        else:
            speak("No word was searched yet.")
    elif command == "meaning":
        if "meanings" in globals():
            definition = meanings[0]["definitions"][0]["definition"]
            speak(f"Meaning: {definition}")
        else:
            speak("Search for a word first.")
    elif command == "link":
        if "meanings" in globals():
            url = f"https://dictionary.com/browse/{word}"
            webbrowser.open(url)
            speak("Opened in browser.")
        else:
            speak("No word to look up.")
    elif command == "example":
        if "meanings" in globals():
            example = meanings[0]["definitions"][0].get("example", "No example found.")
            speak(f"Example: {example}")
        else:
            speak("Search for a word first.")
    else:
        speak("Command not recognized.")

speak("English Dictionary Assistant activated. Say a command.")
try:
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            command = result.get("text", "").lower()
            if command:
                print(f"You: {command}")
                process_command(command)
except KeyboardInterrupt:
    speak("Assistant shutting down.")
    stream.stop_stream()
    stream.close()
    audio.terminate()