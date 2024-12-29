from modelo import Paquete, Reserva

def menu_reservas(id_usuario):
    while True:
        print("----- Menú de Reservas -----")
        print("1) Mostrar Paquetes Disponibles")
        print("2) Hacer una Reserva")
        print("3) Mostrar Mis Reservas")
        print("0) Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Paquete.mostrar_paquetes()
        
        elif opcion == "2":
            id_paquete = int(input("Ingrese el ID del paquete que desea reservar: "))
            fecha_reserva = input("Ingrese la fecha de reserva (YYYY-MM-DD): ")
            reserva = Reserva(id_usuario, id_paquete, fecha_reserva)
            reserva.crear_reserva()
        
        elif opcion == "3":
            Reserva.mostrar_reservas(id_usuario)
        
        elif opcion == "0":
            print("Saliendo del menú de reservas.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")