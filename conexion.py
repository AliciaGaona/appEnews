#  importar libreria para usar sql//
import pyodbc
#srvidor//
server= "localhost"
bd="ExamenPruebaDev"
usuario="sa"
contrasena="1234"

try:
    connectionString = 'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={bd};UID={usuario};PWD={contrasena}'
    print('Conexion exitosa')
   
except:
    print('Error de conexion bd')

pass

#Consulta a base de datos

#creamos un cursor para realizar la consulta
cursor= connectionString.cursor()
cursor.execute("Select * from [appEnews.catalogue.categories];")

persona = cursor.fetchone() #primer resultado del query


#va recorriendo para traer cada row de la tabla de bbase de datos
while persona:
    print(persona)
    persona=cursor.fetchone()

cursor.close()
connectionString.close()

