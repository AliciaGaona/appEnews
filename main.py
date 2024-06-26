from fastapi import FastAPI
import conexionBD
from routes.catalogos import catalogo
#instansems esta clase
app= FastAPI()
#registar una ruta raiz para api http://127.0.0.1:8000
#@ en fast api este decorador registra la funcion, cuando alguien llama a mi ruta raiz ejecuta la funcion que le sigue
app.include_router(catalogo)


