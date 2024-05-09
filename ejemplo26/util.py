import os
def resta(a,b): #parametros
    return a-b
def suma(a=0,b=0):
    return a+b
def multiplicacion(a,b):
    if a !=None and b !=None:
      return a*b
    else:
      return "error"
    
def indeterminado(*args):
   for arg in args:
    if isinstance(arg,str):
        print("es una cadena",arg)

    if isinstance(arg,int):
        print("es entero",arg)

    if isinstance(arg,list):
        print("es una lista",arg)

    if isinstance(arg,dict):
        print("es un diccionario",arg)

def indeterminado2(**args):
   for arg in args:
    print(arg, "=>", args[arg])