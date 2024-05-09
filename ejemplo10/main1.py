import os
os.system("cls")
def ejemplo1():
 for i in range(5):
    print(i, end=", ")
def ejemplo2():
  for i in range(1,10,1):
    print(i,end=" ,")
def ejemplo3():
  for i in range(9,0,-1):
   print(i, end=", ")
def ejemplo4():
  n = int(input("ingrese n "))
  a = 0
  for x in range(1,n+1,1):
   print(x, end= " ,"); a = a + x
   print("suma serie: ", a)
ejemplo1()
ejemplo2()
ejemplo3()
ejemplo4()