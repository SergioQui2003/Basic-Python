notes = []
sum = 0

for i in range(3):
    note = float(input("Introduce la nota " + str(i+1) + ": "))
    if note >= 0.0 and note <= 5.0:
        notes.append(note)
        sum += note
    else:
        print("Por favor ingresa una nota válida (entre 0.0 y 5.0).")
        i -= 1

average = sum / len(notes)

if average >= 3.0:
    print("Aprobó con un promedio de", average)
else:
    print("No aprobó con un promedio de", average)