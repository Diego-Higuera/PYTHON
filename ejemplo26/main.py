import os
from util import resta, suma, multiplicacion, indeterminado, indeterminado2

#argumentos por posicion
def ejemplo1():
    print("resta",resta(5,3)) #argumentos por posicion

#argumentos por nombre
def ejemplo2():
    print("resta", resta(b=3,a=5)) #argumentos por nombre


#parametros por defecto
def ejemplo3():
    print("suma ", suma(5,3))
    print ("suma", ())

#parametros por defecto
def ejemplo4():
    print("multiplicacion", multiplicacion(5,3))
    print("multiplicacion", multiplicacion(5,3))

#parametros indeterminados por posicion
def ejemplo5():
   indeterminado(5,"hola",[1,2,3,4,5],{"id":1,"nombre":"walter"})

#parametros indeterminados por nombre
def ejemplo6():
    indeterminado2(i=5,s="hola",l=[1,2,3,4,5],d={"id":1,"nombre":"walter"})

if __name__ == "__main__":
   ejemplo1()
   ejemplo2()
   ejemplo3()
   ejemplo4()
   ejemplo5()
   ejemplo6()
   os.system("pause")