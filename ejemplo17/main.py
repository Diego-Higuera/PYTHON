import os
os.system("cls")
a = 5
print(type(a))
a = "hola"
print(type(a))
a = 1.72
print(type(a))
a = True
print(type(a))
a = [1,4,7]
print(type(a))
a = {"nombre":"Luis","edad":"23"}
print(type(a))

claves = list(a.keys())
print(type(claves))
if isinstance(claves,dict):
    print("es tipo entero")
else:
    print("no es entero")

    for elemento in list(a.items()):
        print(elemento)

x = len(a.items())
print(x)