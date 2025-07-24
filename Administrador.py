from Usuario import Usuario

class Administrador(Usuario):
    def cambiarContraseña(self, nueva):
        self.Usuario_contrasena = nueva
