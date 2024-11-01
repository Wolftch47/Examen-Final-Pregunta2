from persona import Persona

# Clase Administrativo
class Administrativo(Persona):
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, cargo, departamento):
        super().__init__(nombre, apellido, ci, fecha_nacimiento)
        self.cargo = cargo
        self.departamento = departamento

    def mostrar_datos(self):
        return f"Administrativo: {self.nombre} {self.apellido}, CI: {self.ci}, Fecha de Nacimiento: {self.fecha_nacimiento}, Cargo: {self.cargo}, Departamento: {self.departamento}"
