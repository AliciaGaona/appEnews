import pyodbc 
import os
import dotenv

# cargamos las variables de entorno
dotenv.load_dotenv()  

#variables para conexión BD
server= "ALICIAPC\SQLEXPRESS"
bd="ExamenPruebaDev"
usuario=os.getenv('USUARIO')
contrasena= os.getenv('PASSWD')

#funcion para realizar conexión a BD
def get_connection():
 return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+bd+';UID='+usuario+';PWD='+contrasena)
#print("conexion exitosa")

