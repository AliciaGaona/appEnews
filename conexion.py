#  importar libreria para usar sql//
import pyodbc
#srvidor//
server= "localhost"
bd="ExamenPruebaDev"
usuario="sa"
contrasena="1234"

try:
    connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={bd};UID={usuario};PWD={contrasena}'
    print('Conexion exitosa')
   
except:
    print('Error de conexion bd')

    pass

