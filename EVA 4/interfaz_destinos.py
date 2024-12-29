from modelo import GestorDestinos
from conexion import cursor

# Crear instancia del gestor
gestor_destinos = GestorDestinos(cursor)

# Menú interactivo
def gestor():
    while True:
        print("--- Gestor de Destinos ---")
        print("1. Agregar destino")
        print("2. Mostrar destinos")
        print("3. Modificar destino")
        print("4. Eliminar destino")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del destino: ")
            descripcion = input("Descripción: ")
            actividades = input("Actividades: ")
            costo = float(input("Costo: "))
            gestor_destinos.agregar_destino(nombre, descripcion, actividades, costo)

        elif opcion == "2":
            gestor_destinos.mostrar_destinos()

        elif opcion == "3":
            id_destino = int(input("ID del destino a modificar: "))
            nuevo_nombre = input("Nuevo nombre: ")
            nueva_descripcion = input("Nueva descripción: ")
            nuevas_actividades = input("Nuevas actividades: ")
            
            # Para el nuevo costo, verificamos si el campo está vacío
            nuevo_costo_input = input("Nuevo costo: ")
            if nuevo_costo_input == "":
                nuevo_costo = None  # Si el campo está vacío, no se modifica el costo
            else:
                nuevo_costo = float(nuevo_costo_input)

            gestor_destinos.modificar_destino(id_destino, nuevo_nombre, nueva_descripcion, nuevas_actividades, nuevo_costo)

        elif opcion == "4":
            id_destino = int(input("ID del destino a eliminar: "))
            gestor_destinos.eliminar_destino(id_destino)

        elif opcion == "5":
            print("Saliendo del gestor de destinos.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

gestor()
