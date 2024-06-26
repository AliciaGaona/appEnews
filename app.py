import conexionBD 

#Se utiliza esta seccion para probar conexion, antes de pasar a contruir API y crear modelos
try:  
#variable que guarda la cadena de conexion que trae
  connection = conexionBD.get_connection()
  with connection.cursor() as cursor:#declaro crso para llamara sp
     cursor.execute("exec sp_appEnewscataloguecategories_get")#executo sp
     resultset=cursor.fetchall()#todo lo que traiga el sp quese ejecuto
     for row in resultset:
        print(row)#lo voy imprimiedo

except Exception as ex:
    print(ex)
    pass

