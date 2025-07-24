from Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nombre, correo, id, contrasena, millas=0):
        super().__init__(nombre, correo, id, contrasena)
        self.__millas = int(millas)

    def get_millas(self):
        return self.__millas

    def cambiarContraseña(self, nueva):
        self._contrasena = nueva
