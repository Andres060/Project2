import tkinter as tk
from tkinter import ttk

# Ventana principal
root = tk.Tk()
root.title("StellarJet - Check-in")
root.geometry("900x500")
root.configure(bg="#f29c50")  # Color naranja de fondo

# --------- CABECERA ---------
header = tk.Frame(root, bg="lightgray", height=50)
header.pack(fill="x")

tk.Label(header, text="StellarJet", font=("Helvetica", 18, "bold"), bg="lightgray").pack(side="left", padx=20)

# Menú simulado
tk.Label(header, text="Reservar", font=("Helvetica", 12), bg="lightgray").pack(side="left", padx=20)
tk.Label(header, text="Gestionar", font=("Helvetica", 12), bg="lightgray").pack(side="left", padx=20)
tk.Label(header, text="Check-in", font=("Helvetica", 12, "underline"), bg="lightgray").pack(side="left", padx=20)

# --------- TÍTULO PRINCIPAL ---------
tk.Label(root, text="Check-in", font=("Helvetica", 22, "bold"), bg="#f29c50").pack(pady=10)

# --------- CUERPO PRINCIPAL ---------
main_frame = tk.Frame(root, bg="#f29c50")
main_frame.pack(pady=10)

# --------- IZQUIERDA: Datos del equipaje ---------
left_frame = tk.Frame(main_frame, bg="#f29c50")
left_frame.grid(row=0, column=0, padx=80)

tk.Label(left_frame, text="Cantidad de equipaje:", font=("Helvetica", 14), bg="#f29c50").pack(anchor="w", pady=5)
cantidad_equipaje = tk.Spinbox(left_frame, from_=0, to=10, width=5, font=("Helvetica", 12))
cantidad_equipaje.pack(anchor="w", pady=5)

tk.Label(left_frame, text="Tipo de equipaje:", font=("Helvetica", 14), bg="#f29c50").pack(anchor="w", pady=10)
tipo_equipaje = ttk.Combobox(left_frame, values=["Equipaje de mano", "Equipaje de bodega"], font=("Helvetica", 12))
tipo_equipaje.set("Equipaje de mano")
tipo_equipaje.pack(anchor="w", pady=5)

# --------- DERECHA: Información del vuelo ---------
right_frame = tk.Frame(main_frame, bg="#f29c50")
right_frame.grid(row=0, column=1, padx=80)

tk.Label(right_frame, text="Información del vuelo:", font=("Helvetica", 14, "bold"), bg="#f29c50").pack(pady=5)

info_box = tk.Text(right_frame, height=10, width=40, font=("Helvetica", 12))
info_box.pack(pady=10)

# Simular datos de vuelo cargados
info_box.insert(tk.END,
    "Código vuelo: ABC123\n"
    "Origen: Bogotá\n"
    "Destino: Toronto\n"
    "Horario: 08:00 - 12:00\n"
    "Sillas preferenciales: 10\n"
    "Sillas económicas: 20\n"
    "Millas disponibles: 500"
)
info_box.config(state="disabled")  # Solo lectura

root.mainloop()
