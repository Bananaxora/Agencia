from interfaz_destinos import gestor
from interfaz_usuario import menu_usuario
from interfaz_reservas import menu_reservas
from modelo import Paquete

def main():
    while True:
        print("\n----- Menú Principal -----")
        print("1) Gestionar Destinos (Administrador)")
        print("2) Usuario (Reservas y Registro)")
        print("3) Crear Paquete (Administrador)")
        print("4) Mostrar Paquetes Disponibles")
        print("0) Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestor()  # Llama al gestor de destinos
        elif opcion == "2":
            menu_usuario()  # Llama al menú de usuario
        elif opcion == "3":
            crear_paquete()  # Llama a la función para crear paquetes
        elif opcion == "4":
            Paquete.mostrar_paquetes()  # Muestra paquetes disponibles
        elif opcion == "0":
            print("Gracias por usar la aplicación!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def crear_paquete():
    nombre_paquete = input("Ingrese el nombre del paquete: ")
    fechas_disponibles = input("Ingrese las fechas disponibles (separadas por comas): ")
    precio_total = int(input("Ingrese el precio total: "))
    
    paquete = Paquete(nombre_paquete, fechas_disponibles, precio_total)
    paquete.crear_paquete()
