import os, random
def ejemplo1(lista): #retorna el mayor de una lista de numeros
    return(max(lista))

if __name__ == "__main__":
    print("lista:", [random.randint(1,6) for i in range(10)]) 
    print("mayor:", ejemplo1([random.randint(1,6) for i in range(10)]) )

def ejemplo2():
    print(x)
    x = x+1
    print(x)

if __name__ == "__main__":
    x = 5
    ejemplo2(x)
    print(x)