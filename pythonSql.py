#  tkinter libreria que nos perite usar interfaces graficas //
import tkinter as tk

#importar modulos de tkinter
from tkinter import *
from tkinter import ttk

#modulos de tkinter, para mensaje pop
from tkinter import messagebox

#creo clase para interface
class FormularioClientes:

    #crear funcion
    def Formulario():
        try:
            base=tk()
            base.geometry('1200x500')




        except ValueError as error:
            print("Error al mostrar la interface: {}" .format(error))
