import os
os.system("cls")
def ejemplo1():
    cadena= "en un puerto italiano al pie de las montañas"
    for e in cadena:
        print(e, end=" ")
    print()
    for i in range(len(cadena)):
        print(cadena[i], end=", ")
    print()
    for e in enumerate(cadena):
        print(e)

def ejemplo2():
    cadena = "en un puerto italiano"
    print("subcadena i=5 f=11: ", cadena[5:12:1])
    print("invertir: ", cadena[::-1])
def ejemplo3():
    cadena = "computadora"
    for i in range(len(cadena)):
        print(cadena[0:i+1])
    


ejemplo1()
ejemplo2()
ejemplo3()