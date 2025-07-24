import tkinter as tk
from tkinter import messagebox

# Colores y estilos
BACKGROUND_COLOR = "#69a7d3"
HEADER_COLOR = "#d3d3d3"
FONT = ("Helvetica", 12)
TITLE_FONT = ("Helvetica", 18, "bold")

# Ventana principal
root = tk.Tk()
root.title("StellarJet - Define tu vuelo")
root.geometry("1000x600")
root.configure(bg=BACKGROUND_COLOR)

# Cabecera
header = tk.Frame(root, bg=HEADER_COLOR, height=50)
header.pack(fill="x")

tk.Label(header, text="StellarJet", font=("Helvetica", 20, "bold"), bg=HEADER_COLOR).pack(side="left", padx=20)
for section in ["Reservar", "Gestionar", "Check-in"]:
    tk.Label(header, text=section, font=FONT, bg=HEADER_COLOR).pack(side="left", padx=10)

# Título
tk.Label(root, text="Define tu vuelo", font=TITLE_FONT, bg=BACKGROUND_COLOR).pack(pady=10)

# Filtros de búsqueda
filtros_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
filtros_frame.pack(pady=10)

tk.Label(filtros_frame, text="Origen:", font=FONT, bg=BACKGROUND_COLOR).grid(row=0, column=0)
tk.Entry(filtros_frame, width=15).grid(row=0, column=1, padx=5)

tk.Label(filtros_frame, text="Destino:", font=FONT, bg=BACKGROUND_COLOR).grid(row=0, column=2)
tk.Entry(filtros_frame, width=15).grid(row=0, column=3, padx=5)

tk.Label(filtros_frame, text="Fecha:", font=FONT, bg=BACKGROUND_COLOR).grid(row=0, column=4)
tk.Entry(filtros_frame, width=15).grid(row=0, column=5, padx=5)

tk.Button(filtros_frame, text="Buscar", font=FONT, bg="salmon").grid(row=0, column=6, padx=10)

# Título de horarios
tk.Label(root, text="Horarios:", font=("Helvetica", 14, "bold"), bg=BACKGROUND_COLOR).pack(pady=5)

# Lista de vuelos disponibles
vuelos_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
vuelos_frame.pack(pady=10)

# Vuelos ficticios
vuelos = [
    "08:00 - 10:00 / Sillas Disponibles: 25",
    "10:30 - 12:30 / Sillas Disponibles: 18",
    "14:00 - 16:00 / Sillas Disponibles: 10",
    "17:00 - 19:00 / Sillas Disponibles: 5"
]

def reservar_vuelo(info):
    messagebox.showinfo("Reserva", f"Has seleccionado el vuelo: {info}")

# Mostrar vuelos con botón Reservar
for vuelo in vuelos:
    fila = tk.Frame(vuelos_frame, bg=BACKGROUND_COLOR)
    fila.pack(pady=5)

    entry = tk.Entry(fila, width=50, font=FONT)
    entry.insert(0, vuelo)
    entry.pack(side="left", padx=5)

    tk.Button(fila, text="Reservar", font=FONT, bg="lightgreen",
              command=lambda v=vuelo: reservar_vuelo(v)).pack(side="left", padx=5)

root.mainloop()
