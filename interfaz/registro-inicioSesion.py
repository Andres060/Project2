import tkinter as tk
from tkinter import ttk

# Colores y fuente
BACKGROUND_COLOR = "#d65555"
HEADER_COLOR = "#d3d3d3"
FONT = ("Helvetica", 14)
TITLE_FONT = ("Helvetica", 18, "bold")

# Ventana principal
root = tk.Tk()
root.title("StellarJet")
root.geometry("800x500")
root.configure(bg=BACKGROUND_COLOR)

# Cabecera
header = tk.Frame(root, bg=HEADER_COLOR, height=50)
header.pack(fill="x")

tk.Label(header, text="StellarJet", font=("Helvetica", 20, "bold"), bg=HEADER_COLOR).pack(side="left", padx=20)
tk.Label(header, text="Admin", font=("Helvetica", 12), bg=HEADER_COLOR).pack(side="left", padx=10)

# Mensaje de bienvenida
welcome = tk.Label(root, text="¡Bienvenido a StellarJet!\nTu viaje estelar comienza aquí. Reserva fácil, vuela seguro y disfruta cada destino con confianza.",
                   bg=BACKGROUND_COLOR, font=("Helvetica", 12), fg="black", pady=10)
welcome.pack()

# Contenedor de formularios
form_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
form_frame.pack(expand=True, fill="both", pady=20, padx=20)

# Registrar (izquierda)
register_frame = tk.Frame(form_frame, bg=BACKGROUND_COLOR)
register_frame.pack(side="left", expand=True, fill="both", padx=10)

tk.Label(register_frame, text="Registrarse", font=TITLE_FONT, bg=BACKGROUND_COLOR).pack(pady=10)

tk.Label(register_frame, text="Nombre:", bg=BACKGROUND_COLOR, font=FONT).pack(anchor="w", padx=30)
tk.Entry(register_frame, width=30).pack(pady=2)

tk.Label(register_frame, text="Documento:", bg=BACKGROUND_COLOR, font=FONT).pack(anchor="w", padx=30)
tk.Entry(register_frame, width=30).pack(pady=2)

tk.Label(register_frame, text="Correo:", bg=BACKGROUND_COLOR, font=FONT).pack(anchor="w", padx=30)
tk.Entry(register_frame, width=30).pack(pady=2)

tk.Label(register_frame, text="Contraseña:", bg=BACKGROUND_COLOR, font=FONT).pack(anchor="w", padx=30)
tk.Entry(register_frame, width=30, show="*").pack(pady=2)

# Iniciar sesión (derecha)
login_frame = tk.Frame(form_frame, bg=BACKGROUND_COLOR)
login_frame.pack(side="left", expand=True, fill="both", padx=10)

tk.Label(login_frame, text="Iniciar sesión", font=TITLE_FONT, bg=BACKGROUND_COLOR).pack(pady=10)

tk.Label(login_frame, text="Documento:", bg=BACKGROUND_COLOR, font=FONT).pack(anchor="w", padx=30)
tk.Entry(login_frame, width=30).pack(pady=2)

tk.Label(login_frame, text="Contraseña:", bg=BACKGROUND_COLOR, font=FONT).pack(anchor="w", padx=30)
tk.Entry(login_frame, width=30, show="*").pack(pady=2)

tk.Label(login_frame, text="Cambiar contraseña", bg=BACKGROUND_COLOR, fg="blue", font=("Helvetica", 12, "underline"), cursor="hand2").pack(pady=10)

root.mainloop()
