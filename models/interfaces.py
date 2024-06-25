from pydantic import BaseModel

class Categories(BaseModel):
    id:int
    ref_id:int
    name:str
    alias:str

class Pages(BaseModel):
    id:int
    medio:str
    fecha:str
    id_category:int
    spots:int
    src_link:str
    processing:int

class Copys(BaseModel):
    id:int
    medio:str
    fecha:str
    marca:str
    producto:str
    version:str
    programa:str
    hora:str
    vehiculo:str
    anunciante:str
    tema:str
    id_category:int
    processing:int
    file:str

