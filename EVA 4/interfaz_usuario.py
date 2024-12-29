from interfaz_reservas import menu_reservas
from modelo import Usuario
import getpass as gp

def menu_usuario():
    while True:
        print("----- Bienvenido! -----")
        print("1) Iniciar Sesión                ")
        print("2) Registrarse                   ")
        print("0) Salir                         ")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            nombre = input("Ingrese nombre: ")
            correo = input("Ingrese su correo electrónico: ")
            contrasenia = gp.getpass("Ingrese contraseña: ")
            usuario = Usuario(nombre, correo, contrasenia)
            id_usuario = usuario.acceder()
            if id_usuario:
                print("El ID del usuario actual es:", id_usuario)
                menu_reservas(id_usuario)  # Llama al menú de reservas
        elif opcion == 2:
            nombre = input("Ingrese nombre: ")
            correo = input("Ingrese su correo electrónico: ")
            contrasenia = gp.getpass("Ingrese contraseña: ")
            Usuario(nombre, correo, contrasenia).registrar()
        elif opcion == 0:
            print("Gracias por usar la aplicación!")
            break
        else:
            print("Opción incorrecta!")