import os, sys, mysql.connector, csv

def BaseDatosMysql():
    conexion = None
    try:
        conexion = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="12345678",
        database="tienda")
    except:
        conexion = None
    return conexion

def crear_tabla():
    print('[1] CREAR TABLA TRABAJADOR')
    print('--------------------------')
    conexion = BaseDatosMysql()
    query0 = "DROP DATABASE IF EXISTS tienda"
    query1 = "CREATE DATABASE IF NOT EXISTS tienda"
    query2 = "USE tienda"
    query3 = '''CREATE TABLE IF NOT EXISTS Trabajador(
                            id_trabajador     VARCHAR(6)  NOT NULL PRIMARY KEY,
                            nombre            VARCHAR(20) NOT NULL,
                            apaterno          VARCHAR(30) NOT NULL,
                            tipo_trabajador   INT         NOT NULL,
                            parametros_sueldo VARCHAR(15) NOT NULL
                )'''
    if conexion != None:
       print('OK: CONEXION')
       try:
            cursor = conexion.cursor()

            cursor.execute(query0)
            cursor.execute(query1)
            cursor.execute(query2)
            cursor.execute(query3)

            print('OK: CREATE DATABASE')
            print('OK: CREATE TABLE')
       except:
           print('ERROR: CREATE DATABASE')
           print('ERRORR: CREATE TABLE')
    else:
       print('ERROR: CONEXION')
    os.system('pause')

def insertar():
    print('[2] INSERTAR REGISTROS')
    print('----------------------')
    conexion = BaseDatosMysql()
    if conexion != None:
       print('OK: CONEXION')
       try:
           query = '''INSERT INTO Trabajador(id_trabajador,nombre,apaterno,tipo_trabajador,parametros_sueldo)
                      VALUES(%s,%s,%s,%s,%s)'''
           cursor = conexion.cursor()
           nra = 'C:\\Users\\Curso Tarde\\Documents\\PYTHON\\ejemplo24\\trabajador.csv'
           with open(nra, 'r') as f:
                    filas = csv.reader(f,delimiter=';')
                    filas_lst_lst = list(filas)
                    print(filas_lst_lst)
                    for fila_lst in filas_lst_lst:
                        valores = (fila_lst[0],fila_lst[1],fila_lst[2],fila_lst[3],fila_lst[4])
                        cursor.execute(query,valores)
                        print('OK: INSERT')
                    conexion.commit()
                       
       except:
           print('ERROR: INSERT')
    else:
       print('ERROR: CONEXION')
    os.system('pause')

def mostrar():
    print('[3] MOSTRAR TODOS LOS REGISTROS')
    print('-------------------------------')
    conexion = BaseDatosMysql()
    if  conexion != None:
        print('OK: CONEXION')
        try:
            query = 'SELECT * FROM Trabajador'    # Crear la query
            cursor = conexion.cursor()            # Crear el cursor. Es el que ejecuta las query
            cursor.execute(query)                 # Ejecutar la query. El resultado se guarda en el cursor
            resultado_lst_tup = cursor.fetchall() # Recupear los datos del cursor
            for resultado_tup in resultado_lst_tup:
                print(resultado_tup)
            print('OK: SELECT')
        except:
            print('ERROR: SELECT')
    else:
        print('ERROR: CONEXION')

    os.system('pause')

def actualizar():
    print('[4] ACTUALIZAR UN REGISTRO')
    print('--------------------------')
    conexion = BaseDatosMysql()
    nombre_nuevo = 'Lucrecia'
    id_trabajador_actualizar = 'T1'
    if conexion != None:
       try:
            query = F"UPDATE Trabajador SET nombre = '{nombre_nuevo}' WHERE id_trabajador = '{id_trabajador_actualizar}'"  # Query update  
            cursor = conexion.cursor()                                                                                # Crear cursor
            cursor.execute(query)                                                                                     # Ejecutar query. No producen resultado en el cursor
            conexion.commit() 
            print("ok")
       except:
           print('ERROR: UPDATE')
    else:
       print('ERROR: CONEXION')


    os.system('pause')

def eliminar():
    print('[5] ELIMINAR UN REGISTRO')
    print('------------------------')
    conexion = BaseDatosMysql()
    if conexion != None:
       print('OK: CONEXION')
       id_trabajador = 'T1'
       try:
            query = f"DELETE FROM Trabajador WHERE id_trabajador = '{id_trabajador}'" # Query delete (eliminar todos los registros de la tabla)
            cursor = conexion.cursor()                                           # Crear cursor
            cursor.execute(query)                                                # Ejecutar query. No producen resultado en el cursor
            conexion.commit()                                                    # Confirmar los cambios
            print('OK: DELETE')
       except:   
            print('ERROR: DELETE')
       finally:
            cursor.close()
            conexion.close()

    else:
       print('ERROR: CONEXION')

    os.system('pause')

def buscar():
    print('[6] BUSCAR POR ID DE TRABAJADOR')
    print('-------------------------------')
    conexion = BaseDatosMysql()
    if  conexion != None:
        id_trabajador_buscar = input("ingrese id_trabajador a buscar: ").upper()
        print('OK: CONEXION')
        try:
            query = F"SELECT * FROM Trabajador WHERE id_trabajador = '{id_trabajador_buscar}'"   # Crear la query
            cursor = conexion.cursor()            # Crear el cursor. Es el que ejecuta las query
            cursor.execute(query)                 # Ejecutar la query. El resultado se guarda en el cursor
            resultado_lst_tup = cursor.fetchall() # Recupear los datos del cursor
            if resultado_lst_tup != []:
                for resultado_tup in resultado_lst_tup:
                 print(resultado_tup)
                 print('OK: SELECT')
            else:
               print("id trabajador no existe")
        except:
            print('ERROR: SELECT')
    else:
        print('ERROR: CONEXION')

    os.system('pause')

def salir():
    os.system('cls')
    print('GRACIAS POR SU VISITA')
    sys.exit()

def default():
    pass