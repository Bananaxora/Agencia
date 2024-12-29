import requests
from conexion import cursor
from argon2 import PasswordHasher

class Usuario:

    def __init__(self, nombre, email,  contrasenia):
        self.__nombre = nombre
        self.__email = email
        self.__contrasenia = contrasenia

    def registrar(self):
        ph = PasswordHasher()
        try:
            insert_query = "INSERT INTO USUARIOS (NOMBRE, EMAIL, CONTRASENIA) VALUES (?, ?, ?)"
            password_encode = ph.hash(self.__contrasenia)
            cursor.execute(insert_query, self.__nombre, self.__email, password_encode)
            cursor.commit()
            print(f'Usuario {self.__nombre} registrado exitosamente!')
        except Exception as e:
            print("Error al registrar al usuario.", e)

    def acceder(self):
        ph = PasswordHasher()
        try:
            select_query = "SELECT ID_USUARIO, CONTRASENIA FROM USUARIOS WHERE NOMBRE = ?"
            cursor.execute(select_query, self.__nombre)
            datos = cursor.fetchone()
            if datos:
                ph.verify(datos[1], self.__contrasenia)
                print(f"Sesion iniciada con usuario {self.__nombre}")
                return datos[0]
            else:
                print(f"No se encuentra el usuario {self.__nombre}")
        except Exception as e:
            print("Error al buscar al usuario en la base de datos", e)

class Destino:
    def __init__(self, id_destino, nombre, descripcion, actividades, costo):
        self.id_destino = id_destino
        self.nombre = nombre
        self.descripcion = descripcion
        self.actividades = actividades
        self.costo = costo

    def __str__(self):
        return (f"ID: {self.id_destino}, Nombre: {self.nombre}, Descripción: {self.descripcion}, "
                f"Actividades: {self.actividades}, Costo: {self.costo}")

class GestorDestinos:
    def __init__(self, cursor):
        self.cursor = cursor

    def agregar_destino(self, nombre, descripcion, actividades, costo):
        try:
            self.cursor.execute(
                "INSERT INTO DESTINOS (NOMBRE, DESCRIPCION, ACTIVIDADES, COSTO) VALUES (?, ?, ?, ?)",
                (nombre, descripcion, actividades, costo)
            )
            self.cursor.commit()
            print(f"Destino '{nombre}' agregado correctamente.")
        except Exception as e:
            print("Error al agregar el destino:", e)

    def mostrar_destinos(self):
        try:
            self.cursor.execute("SELECT * FROM DESTINOS")
            destinos = self.cursor.fetchall()
            print("\n--- Lista de Destinos ---")
            if destinos:
                for destino in destinos:
                    print(f"ID: {destino[0]}, Nombre: {destino[1]}, Descripción: {destino[2]}, "
                          f"Actividades: {destino[3]}, Costo: {destino[4]}")
            else:
                print("No hay destinos registrados.")
        except Exception as e:
            print("Error al mostrar los destinos:", e)

    def modificar_destino(self, id_destino, nuevo_nombre, nueva_descripcion, nuevas_actividades, nuevo_costo):
        try:
            self.cursor.execute(
                "UPDATE DESTINOS SET NOMBRE = ?, DESCRIPCION = ?, ACTIVIDADES = ?, COSTO = ? WHERE ID_DESTINO = ?",
                (nuevo_nombre, nueva_descripcion, nuevas_actividades, nuevo_costo, id_destino)
            )
            self.cursor.commit()
            print(f"Destino con ID {id_destino} modificado correctamente.")
        except Exception as e:
            print("Error al modificar el destino:", e)

    def eliminar_destino(self, id_destino):
        try:
            self.cursor.execute("DELETE FROM DESTINOS WHERE ID_DESTINO = ?", (id_destino,))
            self.cursor.commit()
            print(f"Destino con ID {id_destino} eliminado correctamente.")
        except Exception as e:
            print("Error al eliminar el destino:", e)

class Reserva:
    def __init__(self, id_usuario, id_paquete, fecha_reserva, estado="Confirmada"):
        self.id_usuario = id_usuario
        self.id_paquete = id_paquete
        self.fecha_reserva = fecha_reserva
        self.estado = estado

    def crear_reserva(self):
        try:
            insert_query = "INSERT INTO RESERVAS (ID_USUARIO, ID_PAQUETE, FECHA_RESERVA, ESTADO) VALUES (?, ?, ?, ?)"
            cursor.execute(insert_query, (self.id_usuario, self.id_paquete, self.fecha_reserva, self.estado))
            cursor.commit()
            print("Reserva creada exitosamente.")
        except Exception as e:
            print("Error al crear la reserva:", e)

    @staticmethod
    def mostrar_reservas(id_usuario):
        try:
            select_query = "SELECT * FROM RESERVAS WHERE ID_USUARIO = ?"
            cursor.execute(select_query, (id_usuario,))
            reservas = cursor.fetchall()
            if reservas:
                for reserva in reservas:
                    print(f"ID Reserva: {reserva[0]}, ID Paquete: {reserva[2]}, Fecha: {reserva[3]}, Estado: {reserva[4]}")
            else:
                print("No tienes reservas.")
        except Exception as e:
            print("Error al mostrar las reservas:", e)

class Paquete:
    def __init__(self, nombre_paquete, fechas_disponibles, precio_total):
        self.nombre_paquete = nombre_paquete
        self.fechas_disponibles = fechas_disponibles
        self.precio_total = precio_total

    def crear_paquete(self):
        try:
            insert_query = "INSERT INTO PAQUETES (NOMBRE_PAQUETE, FECHAS_DISPONIBLES, PRECIO_TOTAL) VALUES (?, ?, ?)"
            cursor.execute(insert_query, (self.nombre_paquete, self.fechas_disponibles, self.precio_total))
            cursor.commit()
            print(f"Paquete '{self.nombre_paquete}' creado exitosamente.")
        except Exception as e:
            print("Error al crear el paquete:", e)

    @staticmethod
    def mostrar_paquetes():
        try:
            cursor.execute("SELECT * FROM PAQUETES")
            paquetes = cursor.fetchall()
            if paquetes:
                for paquete in paquetes:
                    print(f"ID: {paquete[0]}, Nombre: {paquete[1]}, Fechas: {paquete[2]}, Precio: {paquete[3]}")
            else:
                print("No hay paquetes disponibles.")
        except Exception as e:
            print("Error al mostrar los paquetes:", e)