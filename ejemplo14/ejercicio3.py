import os

os.system("cls")
n = int(input("ingrese numero entero positivo: "))
bandera = True
for i in range(2,n):
    if n % i == 0:
        bandera = False
        break
if bandera:
    print("es primo")
else:
    print("no primo")