import os, re

def validarNumero(numero):
    patron = "[0-9]+|[0-9]+.[0-9]{1,2}"
    correcto = re.fullmatch(patron,numero)
    if correcto:
        return True
    else:
        return False
def sumar():
    print("sumar")
    print("-----")
    n1 = input("ingrese numero 1:")
    n2 = input("ingrese numero 2:")
    if validarNumero(n1) and validarNumero(n2):
        suma = float(n1) + float(n2)
        print("SUMA: ", suma)
    else:
        print("ENTRADA INCORRECTA")
def restar():
    print("restar")
    print("------")
    n1 = input("ingrese numero 1:")
    n2 = input("ingrese numero 2:")
    if validarNumero(n1) and validarNumero(n2):
        restar = float(n1) - float(n2)
        print("RESTA: ", restar)
    else:
        print("ENTRADA INCORRECTA")
def multiplicar():
    print("multiplicar")
    print("-----------")
    n1 = input("ingrese numero 1:")
    n2 = input("ingrese numero 2:")
    if validarNumero(n1) and validarNumero(n2):
        multiplicar = float(n1) * float(n2)
        print("MULTIPLICACION: ", multiplicar)
    else:
        print("ENTRADA INCORRECTA")
def dividir():
    print("dividir")
    print("-------")
    n1 = input("ingrese numero 1:")
    n2 = input("ingrese numero 2:")
    if validarNumero(n1) and validarNumero(n2):
        dividir = float(n1) / float(n2)
        print("DIVISION: ", dividir)
    else:
        print("ENTRADA INCORRECTA")
def potencia():
    print("potencia")
    print("--------")
    n1 = input("ingrese numero 1:")
    n2 = input("ingrese numero 2:")
    if validarNumero(n1) and validarNumero(n2):
        potencia = float(n1) ** float(n2)
        print("POTENCIA: ", potencia)
    else:
        print("ENTRADA INCORRECTA")
def default():
    print("ENTRADA INCORRECTA")

switch_dic = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir,
    "**": potencia
}

def principal():
    while True:
        os.system ("cls")
        clave = input("ingrese operacion (+ - * / ** FIN): ")
        if clave.upper() == "FIN":
            break
        funcion = switch_dic.get(clave,default)
        funcion();os.system("pause")
    os.system("cls")
    print("GRACIAS POR SU VISITA")
principal()