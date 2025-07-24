import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Colores y estilos
BACKGROUND_COLOR = "#99cc99"
HEADER_COLOR = "#d3d3d3"
FONT = ("Helvetica", 12)
TITLE_FONT = ("Helvetica", 18, "bold")

# Crear ventana principal
root = tk.Tk()
root.title("StellarJet - Reserva")
root.geometry("1000x600")
root.configure(bg=BACKGROUND_COLOR)

# Cabecera
header = tk.Frame(root, bg=HEADER_COLOR, height=50)
header.pack(fill="x")

tk.Label(header, text="StellarJet", font=("Helvetica", 20, "bold"), bg=HEADER_COLOR).pack(side="left", padx=20)
for section in ["Reservar", "Gestionar", "Check-in"]:
    tk.Label(header, text=section, font=FONT, bg=HEADER_COLOR).pack(side="left", padx=10)

# Título
tk.Label(root, text="Reserva", font=TITLE_FONT, bg=BACKGROUND_COLOR).pack(pady=10)

# Filtros de vuelo (origen, destino, fecha, pasajeros)
top_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
top_frame.pack(pady=5)

tk.Label(top_frame, text="Origen:", font=FONT, bg=BACKGROUND_COLOR).grid(row=0, column=0)
tk.Entry(top_frame, width=15).grid(row=0, column=1, padx=5)

tk.Label(top_frame, text="Destino:", font=FONT, bg=BACKGROUND_COLOR).grid(row=0, column=2)
tk.Entry(top_frame, width=15).grid(row=0, column=3, padx=5)

tk.Label(top_frame, text="Fecha:", font=FONT, bg=BACKGROUND_COLOR).grid(row=0, column=4)
tk.Entry(top_frame, width=15).grid(row=0, column=5, padx=5)

tk.Label(top_frame, text="Pasajeros (Max 3):", font=FONT, bg=BACKGROUND_COLOR).grid(row=0, column=6)
passenger_spinbox = tk.Spinbox(top_frame, from_=1, to=3, width=5)
passenger_spinbox.grid(row=0, column=7, padx=5)

# Cuerpo de contenido
main_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
main_frame.pack(fill="both", expand=True, padx=20)

# Información de pasajeros
left_frame = tk.Frame(main_frame, bg=BACKGROUND_COLOR)
left_frame.pack(side="left", fill="both", expand=True)

tk.Label(left_frame, text="Información de los pasajeros (No.#):", font=("Helvetica", 14, "bold"), bg=BACKGROUND_COLOR).pack(pady=10)

def crear_formulario_pasajero():
    frame = tk.Frame(left_frame, bg=BACKGROUND_COLOR)
    frame.pack(pady=5)
    
    for label in ["Nombre:", "Apellidos:", "Documento:", "Correo:"]:
        tk.Label(frame, text=label, font=FONT, bg=BACKGROUND_COLOR).pack(anchor="w", padx=10)
        tk.Entry(frame, width=40).pack(pady=2)

# Hasta 3 formularios de pasajeros
for _ in range(2):  # puedes cambiar esto dinámicamente según el Spinbox
    crear_formulario_pasajero()

tk.Button(left_frame, text="Reservar", font=FONT, bg="salmon", command=lambda: messagebox.showinfo("Reserva", "Reserva realizada")).pack(pady=10)

# Información del vuelo y resumen
right_frame = tk.Frame(main_frame, bg=BACKGROUND_COLOR)
right_frame.pack(side="left", fill="both", expand=True, padx=10)

# Información del vuelo
info_vuelo = tk.LabelFrame(right_frame, text="Información del vuelo:", font=FONT, bg=BACKGROUND_COLOR)
info_vuelo.pack(pady=10, fill="x")

for item in [
    "Código vuelo: _______", "Origen: ___________", "Destino: ___________",
    "Horario ___________", "Sillas preferenciales: ___", "Sillas económicas: _____"
]:
    tk.Label(info_vuelo, text=item, font=FONT, bg=BACKGROUND_COLOR).pack(anchor="w", padx=10, pady=2)

# Resumen de reserva
resumen_frame = tk.LabelFrame(right_frame, text="Resumen de reserva:", font=FONT, bg=BACKGROUND_COLOR)
resumen_frame.pack(pady=10, fill="x")

tk.Label(resumen_frame, text="Impuestos...\nCargos...\nTotal a pagar...", font=FONT, bg="lightgray", width=40, height=4).pack(padx=10, pady=5)
tk.Label(resumen_frame, text="Número de reserva: STXXXX", font=FONT, bg=BACKGROUND_COLOR).pack(pady=5)

root.mainloop()
