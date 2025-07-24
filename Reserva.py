from Equipaje import Equipaje
from Pasajero import Pasajero
from typing import List, Dict
import os
import tkinter as tk
from tkinter import messagebox


class Reserva:
    id_counter = 1

    def __init__(self, numero_reserva: str, cliente_doc: str, vuelo_cod: str, pasajeros: List['Pasajero']):
        self._numero_reserva = numero_reserva
        self._cliente_doc = cliente_doc
        self._vuelo_cod = vuelo_cod
        self._pasajeros = pasajeros
        self._check_in_realizado = False
        self._equipaje: List[Equipaje] = []
        self._millas_acumuladas = 0
        self._total = self.calcular_total()

    def calcular_total(self) -> float:
        try:
            return len(self._pasajeros) * 235000
        except Exception:
            self._mostrar_error()
            return 0.0

    def realizar_check_in(self):
        try:
            self._check_in_realizado = True
            self._millas_acumuladas = 500
        except Exception:
            self._mostrar_error()

    def _mostrar_error(self):
        if 'tk' in globals():
            messagebox.showerror("Error", "Ha ocurrido un error, lo sentimos")
        else:
            print("Ha ocurrido un error, lo sentimos")
