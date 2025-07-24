import tkinter as tk
from tkinter import messagebox

class Equipaje:
    def __init__(self, tipo: str, peso: float, volumen: float):
        self._tipo = tipo
        self._peso = peso
        self._volumen = volumen
        self._costo = self.calcular_costo()

    def calcular_costo(self) -> float:
        try:
            if self._tipo == "cabina":
                return 40000
            elif self._tipo == "bodega":
                return self._peso * 1500 + self._volumen * 100
            return 0
        except Exception:
            if 'tk' in globals():
                messagebox.showerror("Error", "Ha ocurrido un error, lo sentimos")
            else:
                print("Ha ocurrido un error, lo sentimos")
            return 0.0
