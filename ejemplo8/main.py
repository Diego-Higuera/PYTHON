import os
os.system("cls")
nota = float(input("ingrese su nota "))
if nota >= 0 and nota < 5:
    mensaje = "suspenso"
elif nota < 7:
    mensaje = "suficiente"
elif nota < 9:
    mensaje = "notable"
elif nota <= 10:
    mensaje = "sobresaliente"
else:
    mensaje = "nota no valida"
print(mensaje)