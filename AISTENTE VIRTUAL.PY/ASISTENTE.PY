import wikipedia
import webbrowser
import datetime
import pyjokes
from pytube import YouTube

def hablar(texto):
    # Aquí iría el código para que el asistente hable el texto
    print(texto)

def buscar_wikipedia(consulta):
    try:
        resultado = wikipedia.summary(consulta, sentences=2)
        hablar("Según Wikipedia, " + resultado)
    except wikipedia.exceptions.PageError:
        hablar("Lo siento, no encontré nada en Wikipedia sobre eso.")

def buscar_videos(consulta):
    try:
        video = YouTube("https://www.youtube.com/results?search_query=" + consulta)
        hablar("Aquí está el primer resultado que encontré en YouTube: " + video.title)
        webbrowser.open(video.url)
    except:
        hablar("Lo siento, no encontré ningún video.")

def contar_chiste():
    chiste = pyjokes.get_joke()
    hablar(chiste)

def decir_fecha_y_hora():
    ahora = datetime.datetime.now()
    hora = ahora.strftime("%H:%M")
    fecha = ahora.strftime("%d/%m/%Y")
    hablar("Hoy es " + fecha + " y son las " + hora)

def abrir_pagina_web(url):
    webbrowser.open(url)

# Aquí comienza el código principal del asistente
while True:
    texto = input("¿En qué puedo ayudarte hoy? ")
    if "buscar en wikipedia" in texto:
        consulta = texto.replace("buscar en wikipedia", "")
        buscar_wikipedia(consulta)
    elif "buscar videos de" in texto:
        consulta = texto.replace("buscar videos de", "")
        buscar_videos(consulta)
    elif "cuenta un chiste" in texto:
        contar_chiste()
    elif "qué hora es" in texto or "qué día es hoy" in texto:
        decir_fecha_y_hora()
    elif "abrir" in texto:
        url = texto.replace("abrir", "")
        abrir_pagina_web(url)
    elif "salir" in texto:
        hablar("Hasta luego.")
        break