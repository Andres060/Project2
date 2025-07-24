import tkinter as tk
from tkinter import messagebox

# Ventana principal
root = tk.Tk()
root.title("StellarJet - Administrador")
root.geometry("1000x600")
root.configure(bg="#5b96a8")  # Fondo azul similar

# --------- CABECERA ---------
header = tk.Frame(root, bg="lightgray", height=50)
header.pack(fill="x")

tk.Label(header, text="StellarJet", font=("Helvetica", 18, "bold"), bg="lightgray").pack(side="left", padx=20)
tk.Label(header, text="Admin", font=("Helvetica", 14), bg="lightgray").pack(side="left")

# --------- TÍTULO PRINCIPAL ---------
tk.Label(root, text="Administrador", font=("Helvetica", 20, "bold"), bg="#5b96a8").pack(pady=10)

# --------- CUERPO ---------
main_frame = tk.Frame(root, bg="#5b96a8")
main_frame.pack(pady=10)

# --------------------- SECCIÓN IZQUIERDA - GESTIONAR VUELOS ---------------------
left_frame = tk.Frame(main_frame, bg="#5b96a8")
left_frame.grid(row=0, column=0, padx=40)

tk.Label(left_frame, text="Gestionar vuelos", font=("Helvetica", 16, "bold"), bg="#5b96a8").pack(pady=10)

campos = [
    "Código de vuelo:", "Origen:", "Destino:",
    "Horario:", "Sillas preferenciales:", "Sillas económicas:"
]
entries = []

for campo in campos:
    tk.Label(left_frame, text=campo, font=("Helvetica", 12), bg="#5b96a8").pack(anchor="w")
    entry = tk.Entry(left_frame, width=30)
    entry.pack(pady=5)
    entries.append(entry)

def agregar_vuelo():
    datos = [e.get() for e in entries]
    if all(datos):
        messagebox.showinfo("Éxito", f"Vuelo {datos[0]} agregado.")
        for e in entries:
            e.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos incompletos", "Por favor llena todos los campos.")

tk.Button(left_frame, text="Agregar", font=("Helvetica", 12), bg="lightblue", command=agregar_vuelo).pack(pady=10)

# --------------------- SECCIÓN DERECHA - CONSULTAR VUELOS ---------------------
right_frame = tk.Frame(main_frame, bg="#5b96a8")
right_frame.grid(row=0, column=1, padx=40)

tk.Label(right_frame, text="Consultar vuelos", font=("Helvetica", 16, "bold"), bg="#5b96a8").pack(pady=10)

search_entry = tk.Entry(right_frame, width=30)
search_entry.insert(0, "Código de vuelo")
search_entry.pack(pady=5)

resultado_texto = tk.Text(right_frame, height=7, width=40, font=("Helvetica", 11))
resultado_texto.pack(pady=10)

def buscar_vuelo():
    codigo = search_entry.get()
    # Simulación de búsqueda (aquí se usaría archivo o base de datos real)
    if codigo == "ABC123":
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.insert(tk.END, 
            "Código vuelo: ABC123\nOrigen: Bogotá\nDestino: Toronto\nHorario: 08:00 - 12:00\nSillas preferenciales: 10\nSillas económicas: 20")
    else:
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.insert(tk.END, "Vuelo no encontrado.")

tk.Button(right_frame, text="Modificar", font=("Helvetica", 12), bg="lightblue", command=buscar_vuelo).pack()

root.mainloop()
