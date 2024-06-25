from fastapi import FastAPI

#instansems esta clase
app= FastAPI()


#registar una ruta raiz para api http://127.0.0.1:8000
#@ en fast api este decorador registra la funcion, cuando alguien llama a mi ruta raiz ejecuta la funcion que le sigue

@app.get("/")
def index():
    return "Hola entre"


@app.get("/getCategories")
def getCategories():
    return "Hola entre"