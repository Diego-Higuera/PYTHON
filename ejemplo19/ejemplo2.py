import os, csv
os.system("cls")
def ejemplo1():
    nra = "C:\Users\Curso Tarde\Desktop\\transacciones.csv"
    try:
        with open(nra, "r") as f:
            filas = csv.reader(f,delimeter=";")
            filas_lst_lst = list(filas)
            for transaccion_lst in filas_lst_lst:
                print(filas)
    except:
        print("error lectura")

ejemplo1()