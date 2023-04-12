import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import random

# Crear una instancia de reconocimiento de voz
r = sr.Recognizer()

# Crear una instancia de conversión de texto a voz
engine = pyttsx3.init()

# Función para convertir texto a voz
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Función para buscar una canción en YouTube
def search_video(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.get().open(url)
    speak(f"Esto es lo que encontré para {query} en YouTube")

# Función para decir la hora
def get_time():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    speak(f"La hora actual es {hour}:{minute}")

# Función para contar un chiste
def tell_joke():
    jokes = [
        "¿Qué le dijo una impresora a otra impresora? Esa hoja es tuya o es impresión mía",
        "¿Por qué los programadores prefieren el café frío? Porque tienen problemas con los loops",
        "¿Cómo se llama un pez que siempre está mintiendo? Un pescador",
        "¿Cómo llamas a un toro que toca la guitarra? Un toro eléctrico"
    ]
    joke = random.choice(jokes)
    speak(joke)

# Capturar el audio del usuario
with sr.Microphone() as source:
    print("Di algo...")
    audio = r.record(source, duration=5)

# Transcribir el audio a texto
try:
    text = r.recognize_google(audio, language='es-ES')
    print("Transcripción:", text)
    if "buscar" in text and "YouTube" in text:
        query = text.split("buscar")[-1].strip()
        search_video(query)
    elif "hora" in text:
        get_time()
    elif "chiste" in text:
        tell_joke()
    else:
        speak("Lo siento, no entiendo lo que quieres decir.")
except sr.UnknownValueError:
    speak("Lo siento, no entendí lo que dijiste.")
