from abc import ABC, abstractmethod

class Usuario(ABC):
    def _init_(self, nombre, correo, id, contrasena):
        self.__nombre = nombre
        self.__correo = correo
        self.__id = id
        self.__contrasena = contrasena

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre
        
    def get_correo(self):
        return self.__correo

    def get_contrasena(self):
        return self.__contrasena

    @abstractmethod
    def cambiarContraseña(self, nueva):
        pass

    def verificar_contrasena(self, contrasena_ingresada):
        return self.__contrasena == contrasena_ingresada
