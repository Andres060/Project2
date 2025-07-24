from Usuario import Usuario

class Cliente(Usuario):
    def __init__(self,nombre, correo, id, contrasena, millas=0):
        super().__init__(nombre, correo, id, contrasena)
        self.__millas = millas
