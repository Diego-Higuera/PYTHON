import os
os.system("cls")
edad = int(input("ingrese su edad "))
mensaje = "ADULTO" if edad >= 18 else "menor"
print(mensaje)