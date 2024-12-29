import pyodbc

class baseDeDatos:

    def __init__(self, driver, servidor, nombre_base_de_datos):
        self.__driver = driver 
        self.__servidor = servidor
        self.__baseDeDatos = nombre_base_de_datos
        self.__connection = None                        
        print(f"Objeto con DB {self.__baseDeDatos} creado!")

    def conectar(self):
        connection_query = f"""
            DRIVER={self.__driver};
            SERVER={self.__servidor};
            DATABASE={self.__baseDeDatos};
            TRUST_CONNECTION=yes;
        """
        try:
            print('Conectando...')
            self.__connection = pyodbc.connect(connection_query)
            print("Conexion exitosa!")
            return self.__connection
        except Exception as error:
            print("Error al conectar", error)

#fuera de la clase
db = baseDeDatos('SQL Server', r'NICO-PC\SQLEXPRESS', 'AGENCIA')
conexionDB = db.conectar()
cursor = conexionDB.cursor()