from estudiante import Estudiante
from administrativo import Administrativo
from docente import Docente

# Función para mostrar el menú
def mostrar_menu():
    print("\nMenu:")
    print("1. Mostrar datos")
    print("2. Agregar nuevo")
    print("3. Borrar")
    print("4. Editar información")
    print("5. Salir")

# Función principal
def main():
    # Crear lista de personas
    personas = [
        Estudiante("Juan", "Pérez", "12345678", "2000-01-01", "Ingeniería", 3),
        Estudiante("Ana", "Gómez", "87654321", "1999-02-02", "Arquitectura", 5),
        Administrativo("Luis", "Fernández", "11111111", "1980-03-03", "Jefe de Recursos Humanos", "Recursos Humanos"),
        Administrativo("María", "López", "22222222", "1985-04-04", "Contador", "Contabilidad"),
        Docente("Carlos", "Martínez", "33333333", "1975-05-05", ["Matemáticas", "Física"], "Mañana"),
        Docente("Laura", "Rodríguez", "44444444", "1982-06-06", ["Química", "Biología"], "Noche"),
        Docente("Pedro", "Sánchez", "55555555", "1990-07-07", ["Historia", "Geografía"], "Mañana"),
    ]

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Mostrar datos
            for persona in personas:
                print(persona.mostrar_datos())
        
        elif opcion == "2":
            # Agregar nuevo
            tipo = input("Seleccione tipo (Estudiante, Administrativo, Docente): ").strip().lower()
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            ci = input("CI: ")
            fecha_nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD): ")

            if tipo == "estudiante":
                carrera = input("Carrera: ")
                semestre = input("Semestre: ")
                personas.append(Estudiante(nombre, apellido, ci, fecha_nacimiento, carrera, semestre))
            elif tipo == "administrativo":
                cargo = input("Cargo: ")
                departamento = input("Departamento: ")
                personas.append(Administrativo(nombre, apellido, ci, fecha_nacimiento, cargo, departamento))
            elif tipo == "docente":
                materias = input("Materias (separadas por coma): ").split(",")
                turno = input("Turno (Mañana/Noche): ")
                personas.append(Docente(nombre, apellido, ci, fecha_nacimiento, [materia.strip() for materia in materias], turno))
            else:
                print("Tipo no válido.")
        
        elif opcion == "3":
            # Borrar
            ci = input("Ingrese CI de la persona a borrar: ")
            personas = [persona for persona in personas if persona.ci != ci]
            print("Persona borrada si existía.")

        elif opcion == "4":
            # Editar información
            ci = input("Ingrese CI de la persona a editar: ")
            for persona in personas:
                if persona.ci == ci:
                    if isinstance(persona, Estudiante):
                        persona.carrera = input("Nueva Carrera: ")
                        persona.semestre = input("Nuevo Semestre: ")
                    elif isinstance(persona, Administrativo):
                        persona.cargo = input("Nuevo Cargo: ")
                        persona.departamento = input("Nuevo Departamento: ")
                    elif isinstance(persona, Docente):
                        materias = input("Nuevas Materias (separadas por coma): ").split(",")
                        persona.materias = [materia.strip() for materia in materias]
                        persona.turno = input("Nuevo Turno (Mañana/Noche): ")
                    print("Información actualizada.")
                    break
            else:
                print("Persona no encontrada.")
        
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
