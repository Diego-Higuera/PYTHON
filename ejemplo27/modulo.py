class Alumno:
    def __init__(self, idAlumno, nombre, edad, estatura):
        self.idAlumno = idAlumno
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura

    def __str__(self):
        return self.idAlumno + ";"+ self.nombre + ";"+ str(self.edad) + ";"+ str(self.estatura) + ";"
 