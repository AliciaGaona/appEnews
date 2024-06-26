# AppEnews

## Instrucciones ⚙️

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

Base de datos

1. Correr script de BD en tu SQL SERVER
2. Agregar tus credenciales de base de datos

En archivo conexionBD.py cambiar valores de variables:

- server = "server"
- bd = "nombre base de datos"
- usuario = "usuario"
- contrasena = "password"

## Correr servidor web uvicorn

```python
 uvicorn main:app --reload
```

##  Rutas y endpoints 

url : http://127.0.0.1:8000 (puede cambiar dependiento tu configuracón local)

| EndPoint | Tipo | 
|----------|----------|
| /getCategories   | get  | 
| /getCopys   | get |
| /getPages    | get  |
| /getAll   | get  |

![image](https://github.com/AliciaGaona/appEnews/assets/99162884/57f84fd5-23d0-4e54-8fb5-b2cd11de051a)
![image](https://github.com/AliciaGaona/appEnews/assets/99162884/c3b33d95-b95f-4dd2-b435-c73f93701474)



## Doucumentcion API(SWAGGER)

url docuentación(swagger) : 127.0.0.1:8000/docs , a tu url le agregas /docs y asi puedes acceder a la docuentación y hacer pruebas de los métodos.

![image](https://github.com/AliciaGaona/appEnews/assets/99162884/b9e82a9d-e657-4cc6-b729-28711803764e)


## Bibliotecas utilizadas

- pymysql


Comando instalación

```python
python -m pip install pyodbc
```

## Procedimientos almacenados

1. sp_appEnewsCatalog_all
2. sp_appEnewscataloguecategories_get
3. sp_appEnewsCatalogueCopys_get
4. sp_appEnewsCataloguePages_get

## Herramientas y tecnologías utilizadas

* SQL SERVER
* Visual code
* Python versión 3.12.4

## Referencias

| URLS | 
|----------|
| [FastAPI](https://fastapi.tiangolo.com/)  |
| [Entorno virtual python](https://docs.python.org/es/3/tutorial/venv.html#creating-virtual-environments) | 
| [pymysql](https://pypi.org/project/PyMySQL/)   |


## FrontEnds

| URLS | 
|----------|
| [Front con Vue](https://github.com/AliciaGaona/appEnewsFront) |
| [Front con React](https://github.com/AliciaGaona/appEnewsFrontwithReact)| 


