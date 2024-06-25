import pyodbc 

server= "ALICIAPC\SQLEXPRESS"
bd="ExamenPruebaDev"
usuario="sa"
contrasena="1234"

#connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={bd};UID={usuario};PWD={contrasena}'

def get_connection():
 return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+bd+';UID='+usuario+';PWD='+contrasena)
#print("conexion exitosa")

