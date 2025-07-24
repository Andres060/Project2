from abc import ABC, abstractmethod
import os
import tkinter as tk
from tkinter import messagebox

class Usuario(ABC):
    def __init__(self, nombre, correo, id, contrasena):
        self.__nombre = nombre
        self.__correo = correo
        self.__id = id
        self.__contrasena = contrasena

    @abstractmethod
    def cambiarContraseña(self, nueva):    
        try:
            self.__contrasena = nueva
        except Exception:
            self._mostrar_error()

    def _mostrar_error(self):
        if 'tk' in globals():
            messagebox.showerror("Error","Ha ocurrido un error, intentalo nuevamente")
