import os
os.system("cls")
lista1 = [1,2,3,4]
lista2 = [1,2,5,6]
lista3 = []
for x in lista1:
    if x in lista2:
        lista3.append(x)
print("lista1: ",lista1)
print("lista2: ",lista2)
print("numeros comunes: ",lista3)