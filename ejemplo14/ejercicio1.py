
import os
while True:
    os.system("cls")

    cadena = input("ingrese cadena: ").upper().strip()
    if cadena == 'FIN':
        break
    partes = cadena.split()
    if len(partes) == 1:
        cadena_invertida =cadena[::-1]
        print("cadena original: ", cadena)
        print("cadena invertida: ", cadena_invertida)
        if cadena == cadena_invertida:
            print ("Palindromo")
        else:
            print ("no palindromo")
    else:
        print ("solo una palabra")