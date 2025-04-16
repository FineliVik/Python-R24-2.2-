import requests
import pyttsx3
import pyaudio
import json
from vosk import Model, KaldiRecognizer
import sys

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 - мужской голос, 1 - женский

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# Инициализация модели Vosk
model = Model("vosk-model-small-ru-0.22")  # Укажите путь к модели Vosk
recognizer = KaldiRecognizer(model, 16000)

# Инициализация PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def get_weather():
    try:
        response = requests.get("https://wttr.in/Saint-Petersburg?format=2")
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Не удалось получить данные о погоде"
    except Exception as e:
        return f"Ошибка при запросе погоды: {str(e)}"

def get_wind():
    try:
        response = requests.get("https://wttr.in/Saint-Petersburg?format=%w")
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Не удалось получить данные о ветре"
    except Exception as e:
        return f"Ошибка при запросе данных о ветре: {str(e)}"

def recommend_walk():
    try:
        temp_response = requests.get("https://wttr.in/Saint-Petersburg?format=%t")
        wind_response = requests.get("https://wttr.in/Saint-Petersburg?format=%w")
        
        if temp_response.status_code == 200 and wind_response.status_code == 200:
            temp = int(temp_response.text.strip().replace('°C', ''))
            wind = int(wind_response.text.strip().replace('km/h', ''))
            
            if temp < 5 or wind > 15:
                return "Прогулка не рекомендуется"
            else:
                return "Прогулка рекомендуется"
        else:
            return "Не удалось получить данные для рекомендации"
    except Exception as e:
        return f"Ошибка при проверке условий для прогулки: {str(e)}"

def find_word(word):
    try:
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if response.status_code == 200:
            data = response.json()
            
            meanings = data[0]['meanings'][0]
            definition = meanings['definitions'][0]['definition']
            
            return f"Определение слова {word}: {definition}"
        else:
            return f"Не удалось найти определение слова {word}"
    except Exception as e:
        return f"Ошибка при поиске слова: {str(e)}"

def process_command(command):
    command = command.lower()
    
    if "погода" in command:
        weather = get_weather()
        speak(f"Текущая погода в Санкт-Петербурге: {weather}")
    elif "ветер" in command:
        wind = get_wind()
        speak(f"Скорость ветра: {wind}")
    elif "прогулка" in command:
        recommendation = recommend_walk()
        speak(recommendation)
    elif "найти" in command:
        word = command.replace("найти", "").strip()
        if word:
            result = find_word(word)
            speak(result)
        else:
            speak("Пожалуйста, укажите слово для поиска")
    else:
        speak("Извините, я не понял команду. Пожалуйста, повторите.")

speak("Голосовой ассистент запущен. Скажите команду.")

try:
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            command = result.get("text", "")
            if command:
                print("Распознанная команда:", command)
                process_command(command)
except KeyboardInterrupt:
    speak("Голосовой ассистент завершает работу.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    sys.exit()