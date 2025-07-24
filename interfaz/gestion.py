import tkinter as tk
from tkinter import messagebox

# Colores y estilos
BACKGROUND_COLOR = "#c06ba3"
HEADER_COLOR = "#d3d3d3"
FONT = ("Helvetica", 12)
TITLE_FONT = ("Helvetica", 18, "bold")

# Funciones de ejemplo
def check_in(reserva):
    messagebox.showinfo("Check-in", f"Check-in realizado para la reserva {reserva}")

def modificar_reserva(reserva):
    messagebox.showinfo("Modificar", f"Modificar reserva {reserva}")

def cancelar_reserva(reserva):
    messagebox.showinfo("Cancelar", f"Reserva {reserva} cancelada")

# Crear ventana
root = tk.Tk()
root.title("StellarJet - Gestionar Reservas")
root.geometry("900x500")
root.configure(bg=BACKGROUND_COLOR)

# Cabecera
header = tk.Frame(root, bg=HEADER_COLOR, height=50)
header.pack(fill="x")

tk.Label(header, text="StellarJet", font=("Helvetica", 20, "bold"), bg=HEADER_COLOR).pack(side="left", padx=20)
for section in ["Reservar", "Gestionar", "Check-in"]:
    tk.Label(header, text=section, font=("Helvetica", 12), bg=HEADER_COLOR).pack(side="left", padx=10)

# Título
tk.Label(root, text="Gestionar", font=TITLE_FONT, bg=BACKGROUND_COLOR).pack(pady=10)

# Contenedor de reservas
reservas_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
reservas_frame.pack(pady=10)

# Simulación de datos de reserva
reservas = [
    "12345 / Fecha: 2025-07-25 / Origen: Medellín / Destino: Toronto",
    "23456 / Fecha: 2025-07-28 / Origen: Bogotá / Destino: Montreal",
    "34567 / Fecha: 2025-08-01 / Origen: Cali / Destino: Vancouver",
    "45678 / Fecha: 2025-08-03 / Origen: Medellín / Destino: Quebec"
]

# Mostrar cada reserva
for reserva in reservas:
    fila = tk.Frame(reservas_frame, bg=BACKGROUND_COLOR)
    fila.pack(pady=5)

    tk.Entry(fila, width=60, font=FONT).insert(0, f"No. Reserva: {reserva}")
    entry = tk.Entry(fila, width=60, font=FONT)
    entry.insert(0, f"No. Reserva: {reserva}")
    entry.pack(side="left", padx=5)

    tk.Button(fila, text="Check-in", bg="lightgreen", font=FONT, command=lambda r=reserva: check_in(r)).pack(side="left", padx=5)
    tk.Button(fila, text="Modificar", bg="lightgray", font=FONT, command=lambda r=reserva: modificar_reserva(r)).pack(side="left", padx=5)
    tk.Button(fila, text="Cancelar", bg="red", fg="white", font=FONT, command=lambda r=reserva: cancelar_reserva(r)).pack(side="left", padx=5)

root.mainloop()
