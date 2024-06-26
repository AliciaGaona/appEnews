# AppEnews

## Instrucciones

Instalar python

[Instalar python](https://www.python.org/downloads/)


Instalar programa de instalación pip

```python
python -m pip install SomePackage
```


Crear entorno virtual para instalar todo lo relacionado con fast Api

```python
python -m venv fastapi-env
```

Activar entorno virtual

```python
fastApi-env\Scripts\activate
```

Asi nos podemos dar cuenta de que se activo el entorno virtual fastApi

![image](https://github.com/AliciaGaona/appEnews/assets/99162884/0417f7f5-43fa-4268-b0da-49269e220785)


Instalar FastAPI

```python
pip install fastapi
```

Fastapi funciona con uvicorn, es un modulo que crea servidor web para ejecutar nuestra api

```python
pip install uvicorn
```


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


## Doucumentcion API(SWAGGER)

url docuentación(swagger) : 127.0.0.1:8000/docs , a tu url le agregas /docs y asi puedes acceder a la docuentación y hacer pruebas de los métodos.

![image](https://github.com/AliciaGaona/appEnews/assets/99162884/b9e82a9d-e657-4cc6-b729-28711803764e)


## Bibliotecas utilizadas

- pymysql


Comando instalación

```python
python -m pip install pyodbc
```

[Pyodbc](https://learn.microsoft.com/es-es/sql/connect/python/pyodbc/python-sql-driver-pyodbc?view=sql-server-ver16)


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

[Front con Vue](https://github.com/AliciaGaona/appEnewsFront)

[Front con React](https://github.com/AliciaGaona/appEnewsFrontwithReact)


