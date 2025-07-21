from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, correo, id, contraseña):
        self.__nombre = nombre
        self.__correo = correo
        self.__id = id
        self.__contraseña = contraseña

    @abstractmethod
    def iniciarSesion(self, nombre, contrasena,):
        pass

    @abstractmethod
    def cambiarContraseña(self, contraseña):
        pass

    @abstractmethod
    def toString(self):
        pass

        