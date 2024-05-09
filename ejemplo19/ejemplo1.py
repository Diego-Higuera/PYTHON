import os
os.system("cls")
def ejemplo1():
    matriz = [[3,4,5],[7,8,9]]
    nf = len(matriz)
    nc = len(matriz[0])
    for i in range(nf):
        for j in range(nc):
            tupla = i,j
            print(tupla,"=",matriz[i][j], end=" ")
        print()

ejemplo1()