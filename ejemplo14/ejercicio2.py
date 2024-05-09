import os
os.system("cls")
def evaluar(palabra):
    palabra = palabra.upper().strip()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return "palindromo"
    else:
        return "no palindromo"
lista_palabras = ["hola","oso","mouse","reconocer"]
for palabra in lista_palabras:
    print("%-12s %-20s" % (palabra,evaluar(palabra)))