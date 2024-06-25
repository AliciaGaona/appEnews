import conexionBD 

#print(conexionBD.get_connection())

try:
  connection = conexionBD.get_connection()
  with connection.cursor() as cursor:#declaro crso para llamara sp
     cursor.execute("exec sp_appEnewscataloguecategories_get")
     resultset=cursor.fetchall()#todo lo que traiga
     for row in resultset:
        print(row)

except Exception as ex:
    print(ex)
    pass

