#evaluar una nota
import os
os.system("cls")
#entrada
nota = int(input ("ingresar nota "))
#procesar
if nota < 5:
    mensaje = "suspenso"
else:
    mensaje = "aprovado"
#salida
print("resultado: " + mensaje)