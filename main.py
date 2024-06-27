from fastapi import FastAPI
import conexionBD
from routes.catalogos import catalogo

from fastapi.middleware.cors import CORSMiddleware

#instansems esta clase
app= FastAPI()

# Se agrega configuración de la política CORS,para poder consumir desde cualquier origin
#  esta configuracion tiene que estar en main.py o no te dará la opción add_middleware

app.add_middleware(CORSMiddleware, allow_origins=['*'])

#registar una ruta raiz para api http://127.0.0.1:8000
#@ en fast api este decorador registra la funcion, cuando alguien llama a mi ruta raiz ejecuta la funcion que le sigue
app.include_router(catalogo)



