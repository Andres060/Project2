import tkinter as tk
from tkinter import messagebox

def mostrar_login(root, sistema, callback_login):
    ventana = tk.Toplevel(root)
    ventana.title("Inicio de Sesión")
    ventana.geometry("300x300")

    tk.Label(ventana, text="Documento:").pack()
    entry_doc = tk.Entry(ventana)
    entry_doc.pack()

    tk.Label(ventana, text="Contraseña:").pack()
    entry_pass = tk.Entry(ventana, show="*")
    entry_pass.pack()

    def login():
        doc = entry_doc.get()
        contra = entry_pass.get()
        usuario = sistema.iniciarSesion(doc, contra)
        if usuario:
            messagebox.showinfo("Éxito", "Sesión iniciada")
            ventana.destroy()
            callback_login(usuario)
        else:
            messagebox.showerror("Error", "Datos incorrectos")

    def registrar():
        # Aquí puedes abrir otra ventana para registrar (te ayudo si quieres)
        messagebox.showinfo("Registrar", "Función de registro aún no implementada")

    tk.Button(ventana, text="Iniciar Sesión", command=login).pack(pady=5)
    tk.Button(ventana, text="Registrarse", command=registrar).pack()

