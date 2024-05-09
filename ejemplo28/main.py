import os, sqlite3, csv
rutaarchivosqlite = "C:\\Users\\Curso Tarde\\Documents\\PYTHON\\ejemplo30\\tienda.sqlite"
if os.path.exists(rutaarchivosqlite):
    os.remove(rutaarchivosqlite)
    print("ok: archivo sqlite eliminado")
nra = "C:\\Users\\Curso Tarde\\Documents\\PYTHON\\ejemplo30\\tienda.sqlite"
#nra = "C:\\MISQLITE\\tienda.sqlite"
conexion = sqlite3.connect(nra)

cursor = conexion.cursor()
query1 = '''CREATE TABLE IF NOT EXISTS Trabajador(
                 id_trabajador     VARCHAR(6)  NOT NULL PRIMARY KEY,
                 nombre            VARCHAR(20) NOT NULL,
                 apaterno          VARCHAR(30) NOT NULL,
                 tipo_trabajador   INT         NOT NULL,
                 parametros_sueldo VARCHAR(15) NOT NULL
               )'''
cursor.execute(query1)

print("leer archivo csv y grabar en tabla trabajador")
nra = "C:\\Users\\Curso Tarde\\Documents\\PYTHON\\ejemplo30\\trabajador.csv"
query2 = '''INSERT INTO Trabajador(id_trabajador,nombre,apaterno,tipo_trabajador,parametros_sueldo)
                VALUES(?,?,?,?,?)'''
with open(nra, "r") as f:
    resultado = csv.reader(f,delimiter=';')
    filas_lst_lst = list(resultado)
    #print(filas_lst_lst)
    for lista in filas_lst_lst:
        id_trabajador = lista[0]
        nombre = lista[1]
        apaterno = lista[2]
        tipo_trabajador = lista[3]
        parametros_sueldo = lista[4]
        valores = (id_trabajador,nombre,apaterno,tipo_trabajador,parametros_sueldo)
        cursor.execute(query2,valores)
    conexion.commit()
    print("ok: insert")

print("MOSTRAR TODOS LOS REGISTROS DE LA TABLA TRABAJADOR")
print("--------------------------------------------------")
query3 = "SELECT * FROM Trabajador"
cursor.execute(query3)
resultado_lst_tup = cursor.fetchall()
for tupla in resultado_lst_tup:
    print(tupla)

print("ACTUALIZAR UN REGISTRO DE LA TABLA TRABAJADOR")
print("---------------------------------------------")
nombre_nuevo = 'Arturo'
id_trabajador_actualizar = 'T2'
query4 = query = F"UPDATE Trabajador SET nombre = '{nombre_nuevo}' WHERE id_trabajador = '{id_trabajador_actualizar}'"
cursor.execute(query4)
conexion.commit()
print('OK: UPDATE\n')