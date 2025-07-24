import tkinter as tk
from tkinter import messagebox
from Sistema import Sistema
from Cliente import Cliente

class App:
    def __init__(self, root):
        self.root = root
        self.sistema = Sistema()
        self.sistema.cargar_datos() # Carga los datos de vuelos.txt y clientes.txt al iniciar

        self.root.title("StellarJet Airlines")
        self.root.geometry("800x500")

        self.usuario_actual = None
        
        self.mostrar_login_registro()

    def mostrar_login_registro(self):
        self.limpiar_ventana()
        
        #Interfaz copiada de tu archivo registro-inicioSesion.py
        self.root.configure(bg="#d65555")
        
        header = tk.Frame(self.root, bg="#d3d3d3", height=50)
        header.pack(fill="x")
        tk.Label(header, text="StellarJet", font=("Helvetica", 20, "bold"), bg="#d3d3d3").pack(side="left", padx=20)
        
        form_frame = tk.Frame(self.root, bg="#d65555")
        form_frame.pack(expand=True, fill="both", pady=20, padx=20)
        
        # --- Registrar (izquierda) ---
        register_frame = tk.Frame(form_frame, bg="#d65555")
        register_frame.pack(side="left", expand=True, fill="both", padx=10)
        tk.Label(register_frame, text="Registrarse", font=("Helvetica", 18, "bold"), bg="#d65555").pack(pady=10)
        
        tk.Label(register_frame, text="Nombre:", bg="#d65555", font=("Helvetica", 14)).pack(anchor="w", padx=30)
        entry_reg_nombre = tk.Entry(register_frame, width=30)
        entry_reg_nombre.pack(pady=2)
        
        tk.Label(register_frame, text="Documento:", bg="#d65555", font=("Helvetica", 14)).pack(anchor="w", padx=30)
        entry_reg_doc = tk.Entry(register_frame, width=30)
        entry_reg_doc.pack(pady=2)

        tk.Label(register_frame, text="Correo:", bg="#d65555", font=("Helvetica", 14)).pack(anchor="w", padx=30)
        entry_reg_correo = tk.Entry(register_frame, width=30)
        entry_reg_correo.pack(pady=2)

        tk.Label(register_frame, text="Contraseña:", bg="#d65555", font=("Helvetica", 14)).pack(anchor="w", padx=30)
        entry_reg_pass = tk.Entry(register_frame, width=30, show="*")
        entry_reg_pass.pack(pady=2)
        
        tk.Button(register_frame, text="Registrar", command=lambda: self.handle_registro(
            entry_reg_nombre.get(), entry_reg_correo.get(), entry_reg_doc.get(), entry_reg_pass.get()
        )).pack(pady=20)

        # --- Iniciar sesión (derecha) ---
        login_frame = tk.Frame(form_frame, bg="#d65555")
        login_frame.pack(side="left", expand=True, fill="both", padx=10)
        tk.Label(login_frame, text="Iniciar sesión", font=("Helvetica", 18, "bold"), bg="#d65555").pack(pady=10)
        
        tk.Label(login_frame, text="Documento:", bg="#d65555", font=("Helvetica", 14)).pack(anchor="w", padx=30)
        entry_login_doc = tk.Entry(login_frame, width=30)
        entry_login_doc.pack(pady=2)

        tk.Label(login_frame, text="Contraseña:", bg="#d65555", font=("Helvetica", 14)).pack(anchor="w", padx=30)
        entry_login_pass = tk.Entry(login_frame, width=30, show="*")
        entry_login_pass.pack(pady=2)
        
        tk.Button(login_frame, text="Ingresar", command=lambda: self.handle_login(
            entry_login_doc.get(), entry_login_pass.get()
        )).pack(pady=20)

    def handle_registro(self, nombre, correo, doc, contrasena):
        if not nombre or not correo or not doc or not contrasena:
            messagebox.showwarning("Campos incompletos", "Por favor, llene todos los campos para registrarse.")
            return
        
        if self.sistema.registrar_cliente(nombre, correo, doc, contrasena):
            self.sistema.guardar_datos()
            messagebox.showinfo("Registro Exitoso", f"¡Bienvenido, {nombre}! Ahora puedes iniciar sesión.")
        else:
            messagebox.showerror("Error de Registro", f"El usuario con documento {doc} ya existe.")

    def handle_login(self, doc, contrasena):
        usuario = self.sistema.iniciar_sesion(doc, contrasena)
        if usuario:
            self.usuario_actual = usuario
            messagebox.showinfo("Inicio de Sesión Exitoso", f"¡Bienvenido de nuevo, {self.usuario_actual.get_nombre()}!")
            self.mostrar_menu_principal() # Redirigir al menú principal
        else:
            messagebox.showerror("Error de Inicio de Sesión", "Documento o contraseña incorrectos.")

    def mostrar_menu_principal(self):
        self.limpiar_ventana()
        # Aquí iría el código para mostrar la ventana de buscar vuelos.
        # Por simplicidad, ponemos un mensaje y un botón para cerrar sesión.
        tk.Label(self.root, text=f"Menú Principal - Usuario: {self.usuario_actual.get_nombre()}", font=("Helvetica", 20)).pack(pady=50)
        
        # Aquí llamarías a las otras ventanas que diseñaste (buscadorDeVuelos, gestion, etc.)
        
        tk.Button(self.root, text="Cerrar Sesión", command=self.handle_logout).pack(pady=20)
        
    def handle_logout(self):
        self.usuario_actual = None
        self.sistema.guardar_datos() # Guarda cualquier cambio antes de salir
        self.mostrar_login_registro()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
