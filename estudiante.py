from persona import Persona

# Clase Estudiante
class Estudiante(Persona):
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, carrera, semestre):
        super().__init__(nombre, apellido, ci, fecha_nacimiento)
        self.carrera = carrera
        self.semestre = semestre

    def mostrar_datos(self):
        return f"Estudiante: {self.nombre} {self.apellido}, CI: {self.ci}, Fecha de Nacimiento: {self.fecha_nacimiento}, Carrera: {self.carrera}, Semestre: {self.semestre}"
