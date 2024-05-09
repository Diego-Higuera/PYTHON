import os, re
os.system("cls")
def ejemplo1():
    os.system("cls")
    print("reconocer numeros enteros")
    print("-------------------------")
    patron = "\d+" #1, 5, 2223, 4855484...
    #patron = [0-9]
    while True:
        print("ingresar numero entero: ")
        numero = input()
        correcto = re.fullmatch(patron,numero)
        if correcto:
           print("es un numero entero")
        else:
           print("no es un numero entero")

def ejemplo2():
    os.system("cls")
    print("reconocer todo lo que no sea un digito")
    print("-------------------------")
    patron = "\\D+"
    while True:
        print("ingresar cadena: ")
        numero = input()
        correcto = re.fullmatch(patron,numero)
        if correcto:
           print("no tiene ningun digito")
        else:
           print("si tiene un digito")

def ejemplo3():
    os.system("cls")
    print("reconocer todo lo que no sea una vocal")
    print("-------------------------")
    patron = "[^aeiouAEIOU]+"
    while True:
        print("ingresar cadena: ")
        numero = input()
        correcto = re.fullmatch(patron,numero)
        if correcto:
           print("no tiene ninguna vocal")
        else:
           print("si tiene una vocal")

def ejemplo4():
    os.system("cls")
    print("reconocer espacios en blanco")
    print("-------------------------")
    patron = "[^\s]+"
    while True:
        print("ingresar cadena: ")
        numero = input()
        correcto = re.fullmatch(patron,numero)
        if correcto:
           print("no es una oracion")
        else:
           print("es una oracion")

def ejemplo5():
    os.system("cls")
    print("reconocer CADENAS QUE INICIAN CON A Y LUEGO SOLO 2 CARACTERES MAS")
    print("-------------------------")
    patron = "A.." # "."= CUALQUIER CARACTER
    while True:
        print("ingresar cadena: ")
        numero = input()
        correcto = re.fullmatch(patron,numero)
        if correcto:
           print("SI CUMPLE")
        else:
           print("NO CUMPLE")

def ejemplo6():
    os.system("cls")
    print("reconocer CADENAS QUE INICIAN CON A Y LUEGO UNO O NINGUN CARACTER")
    print("-------------------------")
    patron = "A.." 
    while True:
        print("ingresar cadena: ")
        numero = input()
        correcto = re.fullmatch(patron,numero)
        if correcto:
           print("SI CUMPLE")
        else:
           print("NO CUMPLE")  

def ejemplo7():
    os.system("cls")
    #cadena = "hola 1234 como estas 345 tengo 23"
    cadena1 = "maria@hotmail.com como estas carlos@gmail.com en un puerto arturo@gmail.com por lo tanto jesus@hotmail.com"
    p = re.compile("[a-z]+@hotmail|[a-z]+@gmail.com")
    lista = p.findall(cadena1)
    print(lista)

ejemplo7()