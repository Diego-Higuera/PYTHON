import os, re

español_dic = {
               "+": "sumar",
               "-": "restar",
               "*": "multiplicar",
               "/": "dividir",
               "**": "potencia"
              }
ingles_dic = {
               "+": "add",
               "-": "substract",
               "*": "multiply",
               "/": "divide",
               "**": "power"
             }
def validar_entrada(idioma):
    patron = "(ESPAÑOL|INGLES)"
    correcto = re.fullmatch(patron,idioma)
    return correcto
def principal():
    os.system("cls")
    idioma = input("ingrese idioma (español o ingles)").upper()
    if validar_entrada(idioma):
        if idioma == "ESPAÑOL":
            idioma_dic = español_dic.copy()
        else:
            idioma_dic = ingles_dic.copy()
        for tupla in list(idioma_dic.items()):
            print("%-4s %-10s" % (tupla[0],tupla[1]))
    else:
        print("entrada incorrecta")
principal()