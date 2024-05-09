import os
os.system("cls")
for n in range(2,101):
    bandera = True
    for i in range(2,n):
        if n % i == 0:
            bandera = False
            break
    if bandera:
        print(n, " es primo")
    #else:
        #print(n, " no primo")