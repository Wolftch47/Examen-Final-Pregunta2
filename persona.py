from abc import ABC, abstractmethod

# Clase abstracta Persona
class Persona(ABC):
    def __init__(self, nombre, apellido, ci, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.fecha_nacimiento = fecha_nacimiento

    @abstractmethod
    def mostrar_datos(self):
        pass
