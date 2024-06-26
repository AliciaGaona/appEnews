from fastapi import APIRouter
import conexionBD 
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
import models.interfaces as models
from fastapi.middleware.cors import CORSMiddleware

catalogo= APIRouter()


# Se agrega configuración de la política CORS, para poder consumir api desde mi front, ya que esta marcando problemas
# catalogo.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
#     allow_methods=["*"],  # Permitir todos los métodos HTTP
#     allow_headers=["*"],  # Permitir todos los encabezados
# )


@catalogo.get("/")
def index():
    return "Hola entre"


@catalogo.get("/getCategories", response_model=List[models.Categories])
def get_Categories():
    try:
        connection = conexionBD.get_connection()
        cursor=connection.cursor()
        # Ejecuta el procedimiento almacenado
        sql = 'exec sp_appEnewscataloguecategories_get'
        cursor.execute(sql)
        result=cursor.fetchall()
        #serializar_resultado= jsonable_encoder(result)
        #return JSONResponse(content=serializar_resultado)
        return result
    except Exception as e:
        return JSONResponse(content={"error":str(e)}, status_code=500)
    pass


@catalogo.get("/getCopys", response_model=List[models.Copys])
def get_Categories():
    try:
        connection = conexionBD.get_connection()
        cursor=connection.cursor()
        # Ejecuta el procedimiento almacenado
        sql = 'exec sp_appEnewsCatalogueCopys_get'
        cursor.execute(sql)
        result=cursor.fetchall()
        return result
    except Exception as e:
        return JSONResponse(content={"error":str(e)}, status_code=500)
    pass

@catalogo.get("/getPages", response_model=List[models.Pages])
def get_Categories():
    try:
        connection = conexionBD.get_connection()
        cursor=connection.cursor()
        # Ejecuta el procedimiento almacenado
        sql = 'exec sp_appEnewsCataloguePages_get'
        cursor.execute(sql)
        result=cursor.fetchall()
        return result
    except Exception as e:
        return JSONResponse(content={"error":str(e)}, status_code=500)
    pass


@catalogo.get("/getAll", response_model=List[models.All])
def get_All():
    try:
        connection = conexionBD.get_connection()
        cursor=connection.cursor()
        # Ejecuta el procedimiento almacenado
        sql = 'exec sp_appEnewsCatalog_all'
        cursor.execute(sql)
        result=cursor.fetchall()
        return result
    except Exception as e:
        return JSONResponse(content={"error":str(e)}, status_code=500)
    pass
