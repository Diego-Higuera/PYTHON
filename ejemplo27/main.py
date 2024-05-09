import os
import modulo

def llenar_lista_alumnos(alumnos_lst):
    a1 = modulo.Alumno("A1","Miguel",23,1.72)
    a2 = modulo.Alumno("A2","Carlos",22,1.71)
    alumnos_lst.append(a1)
    alumnos_lst.append(a2)

def eliminar_alumno(id,alumnos_lst):
    i = 0
    for alumno in alumnos_lst:
        if alumno.idAlumno == id:
            del alumnos_lst[i]
            i = i + 1

def mostrar_lista_alumnos(alumnos_lst):
    for alumno in alumnos_lst:
        print(alumno)
if __name__ == "__main__":
    alumnos_lst = []
    llenar_lista_alumnos(alumnos_lst)
    eliminar_alumno("A1",alumnos_lst)
    mostrar_lista_alumnos(alumnos_lst)