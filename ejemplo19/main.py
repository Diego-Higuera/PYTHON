import os
os.system("cls")
def ejemplo1():
    tupla = (1,2,3) #no se puede modificar
    lista = [1,2,3] #se puede modificar
    del lista[0]
    print(lista)

ejemplo1()

def ejemplo2():
    #formas de crear una tupla
    #1. usando parentesis
    tupla = (1,2,"hola",1.72,(2),[1,2,3],{"a":1,"b":4})
    #2. usando la funcion tuple
    lista = [8,9,3]
    tupla = tuple(lista)
    print(tupla)
    diccionario = {"a":1,"b":2}
    tupla = tuple(diccionario)
    print(tupla)
    #3. usando la tupla vacia
    tupla = ()
    e = (1)
    tupla = tupla + (e)
    print(tupla)
    #4. retorno de una funcion
    tupla = divmod(20,3)
    print(tupla)
    #5. empaquetado de tuplas
    tupla = 8, 5, "hola"
    print(tupla)
    #6. desempaquetar tuplas
    a,b,c = 11,12,13
    tupla = a,b,c
    print(tupla)

def ejemplo3():
    diccionario = {"a":1,"b":2}
    lista_tuplas = list(diccionario.items())
    print(lista_tuplas)
    for e in lista_tuplas:
        print(e)

def informacion():
    nombre = "miguel"
    edad = 23
    estatura = 1.72
    return nombre, edad, estatura


def ejemplo4():
    print(informacion()[1])

def ejemplo5():
    cadena = "hola mundo"
    tupla = tuple(cadena)
    #recorrer por elemento
    for e in tupla:
        print(e, end=" ")
    print()
    #recorrer por indice
    for i in range(len(tupla)):
        print(tupla[i], end=" ")
    #tomar segmentos
    print()
    print(tupla[0:4])

ejemplo5()