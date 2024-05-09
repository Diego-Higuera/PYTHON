import os, operacionesCRUD as o

def ejecutar_query(query, conexion):
        cursor = conexion.cursor()
        cursor.execute(query)
        cursor.close()
        print("ok base de datos")
        os.system("pause")

def main():
    os.system("cls")
    conexion = o.BaseDatosMysql1()
    if conexion != None:
        ejecutar_query("DROP DATABASE IF EXISTS tienda",conexion)
        ejecutar_query("CREATE DATABASE IF NOT EXISTS tienda",conexion)
        ejecutar_query("USE tienda",conexion)
        ejecutar_query('''CREATE TABLE IF NOT EXISTS Trabajador(
                            id_trabajador     VARCHAR(6)  NOT NULL PRIMARY KEY,
                            nombre            VARCHAR(20) NOT NULL,
                            apaterno          VARCHAR(30) NOT NULL,
                            tipo_trabajador   INT         NOT NULL,
                            parametros_sueldo VARCHAR(15) NOT NULL)''',conexion)
        conexion.close()
    else:
         print("error de conexion")

if __name__ == "__main__":
   main()