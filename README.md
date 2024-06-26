# Construcción de API con Python y fastAPI

## Instrucciones antes de correr proyecto ⚙️

1. Instalar python

[Instalar python](https://www.python.org/downloads/)


2. Instalar programa de instalación pip

```python
python -m pip install SomePackage
```


3. Crear entorno virtual para instalar todo lo relacionado con fastApi

```python
python -m venv fastapi-env
```

4. Activar entorno virtual

```python
fastApi-env\Scripts\activate
```

Asi nos podemos dar cuenta de que se activo el entorno virtual fastApi

![image](https://github.com/AliciaGaona/appEnews/assets/99162884/0417f7f5-43fa-4268-b0da-49269e220785)


5. Instalar FastAPI

```python
pip install fastapi
```

Fastapi funciona con uvicorn, es un modulo que crea servidor web para ejecutar nuestra api

```python
pip install uvicorn
```

6. Instalar pymysql

```python
pip install pymysql
```

## Base de datos 🗂️

1. Correr script de BD en tu SQL SERVER, script se enviará en adjuntos de correo (script_ExamenPruebaDev)
2. Agregar tus credenciales de base de datos

En archivo conexionBD.py cambiar valores de variables:

- server = "server"
- bd = "nombre base de datos"
- usuario = "usuario"
- contrasena = "password"

## Iniciar proyecto 🚀

1. Activar entorno virtual

```python
fastApi-env\Scripts\activate
```
2. Correr servidor

con localhost
   
```python
 uvicorn main:app --reload --host localhost --port 8000
```


![image](https://github.com/AliciaGaona/appEnews/assets/99162884/5d151081-9f1b-4af3-a54b-0b7f7023c6bc)

En esta línea viene la url que utilizó oara correr, en este caso

 Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

##  Rutas y endpoints 🚀

url : http://localhost:8000 (puede cambiar dependiento tu configuracón local)

| EndPoint | Tipo | 
|----------|----------|
| /getCategories   | get  | 
| /getCopys   | get |
| /getPages    | get  |
| /getAll   | get  |
| /docs  | documentación  |

![image](https://github.com/AliciaGaona/appEnews/assets/99162884/57f84fd5-23d0-4e54-8fb5-b2cd11de051a)
![image](https://github.com/AliciaGaona/appEnews/assets/99162884/c3b33d95-b95f-4dd2-b435-c73f93701474)


## Doucumentcion API(SWAGGER) 🚀

url docuentación(swagger) : 127.0.0.1:8000/docs , a tu url le agregas /docs y asi puedes acceder a la docuentación y hacer pruebas de los métodos.

![image](https://github.com/AliciaGaona/appEnews/assets/99162884/b9e82a9d-e657-4cc6-b729-28711803764e)


## Bibliotecas utilizadas 📋

- pymysql
- Framework FastAPI


Comando instalación

```python
python -m pip install pyodbc
```

## Test (Postman) 🚀

![image](https://github.com/AliciaGaona/appEnews/assets/99162884/a3820417-8af3-4510-b043-6751d7db62ef)


## Procedimientos almacenados 🚀

1. sp_appEnewsCatalog_all
2. sp_appEnewscataloguecategories_get
3. sp_appEnewsCatalogueCopys_get
4. sp_appEnewsCataloguePages_get

## Herramientas y tecnologías utilizadas 🔧

* SQL SERVER
* Visual code
* Python versión 3.12.4

## Referencias 🔧

| URLS | 
|----------|
| [FastAPI](https://fastapi.tiangolo.com/)  |
| [Entorno virtual python](https://docs.python.org/es/3/tutorial/venv.html#creating-virtual-environments) | 
| [pymysql](https://pypi.org/project/PyMySQL/)   |


## FrontEnds 🚀

| URLS | 
|----------|
| [Front con Vue](https://github.com/AliciaGaona/appEnewsFront) |
| [Front con React](https://github.com/AliciaGaona/appEnewsFrontwithReact)| 

## En proceso, bugs 🛠️🔎

Bug 1, descripción: Hay un tema en la configuracion del CORS, ya que las pruebas todo ok, pero si cualquier front (se intento con React, Vue y javaScript puro) quiere acceder el CORS lo bloquea, ya que tinenen origins distintos.

![image](https://github.com/AliciaGaona/appEnews/assets/99162884/96345273-55b5-4141-bc3c-caad0b2383f7)


Posible solución 1: revisar como editar la configuración de la API para que corra el servidor con localhost y no con la ip, para correr en local.

comando para obligar a correr en mi localhost y no ip

```phyton
uvicorn main:app --port=8000 --host=localhost --reload  
```

Estatus: Se realiza, aunque corra con localhost, sigue marcando error en CORS, al intentar acceder.


Posible solución 2: 
La solución de la documentación y de lo encontrado, sugiere usar middleware, pero al importarlo este no me da la opción disponible de "add_middleware", tambien se intento usar middleware como clase.

El problema es que esta en un archivo que no es el raiz, app.py o main.py, se probará pasar todos los métodos a api o main, ya que en esos dos si acepta como valido el 
"add_middleware"

archivo: catalogos.py

```phyton
from fastapi.middleware.cors import CORSMiddleware

# Se agrega configuración de la política CORS, para poder consumir api desde mi front, ya que esta marcando problemas
# catalogo.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
#     allow_methods=["*"],  # Permitir todos los métodos HTTP
#     allow_headers=["*"],  # Permitir todos los encabezados
# )

```

Estatus: Resuelto, este tipo de configuración siempre se debe hacer en su raiz main.py, como lo estaba importando  fuera de este archivo, no lo estaba importando con todas las propiedades, se importa en main.py y se le indica por comando al servidor que lo corra sobre localhost, se pueba en consoal de desarrollo.

![image](https://github.com/AliciaGaona/appEnews/assets/99162884/0044f9c2-6b62-40ef-9327-3657364ac544)


```phyton
uvicorn main:app --reload --host localhost --port 8000
```

![image](https://github.com/AliciaGaona/appEnews/assets/99162884/3ac4e2a2-f085-4108-8256-682cb8dfa119)


