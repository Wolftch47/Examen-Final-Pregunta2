from persona import Persona

# Clase Docente
class Docente(Persona):
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, materias, turno):
        super().__init__(nombre, apellido, ci, fecha_nacimiento)
        self.materias = materias
        self.turno = turno

    def mostrar_datos(self):
        return f"Docente: {self.nombre} {self.apellido}, CI: {self.ci}, Fecha de Nacimiento: {self.fecha_nacimiento}, Materias: {', '.join(self.materias)}, Turno: {self.turno}"
