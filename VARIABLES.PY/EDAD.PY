import datetime

año_actual = datetime.datetime.now().year
año_nacimiento = int(input("Su año de nacimiento: "))
año = año_actual - año_nacimiento
print("Su edad es:", año, "años")