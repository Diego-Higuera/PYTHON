import os
os.system("cls")
def ejemplo1():
    lista =[0] * 3
    print(lista)
    lista.append(7)
    lista.append("hola")
    lista.append(True)
    lista.append(1.5)
    print(lista)
    lista.clear()
    print(lista)
def ejemplo2():
    lista =[5,8,9,10,2,1]
    lista.append([2,3])
    print(lista)
    for e in lista:
        if isinstance(e,int):
         if e % 2 == 0:
            print(e)
         else:
            pass

ejemplo1()
ejemplo2()