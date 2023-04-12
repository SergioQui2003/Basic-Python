# Solicitar tiempo en segundos y transformar a horas y minutos

def tiempo_en_segundos(segundos):
# Defino cuantos segundos por hora 
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    return f"{horas} horas y {minutos} minutos"

segundos = 7200
print(tiempo_en_segundos(segundos))