from typing import List, Dict
import os
import tkinter as tk
from tkinter import messagebox

class Vuelo:
    def __init__(self, codigo: str, origen: str, destino: str, horario: str,
                 sillas_preferencial: int, sillas_economica: int):
        self._codigo = codigo
        self._origen = origen
        self._destino = destino
        self._horario = horario
        self._sillas_preferencial = sillas_preferencial
        self._sillas_economica = sillas_economica

    def obtener_disponibilidad(self) -> Dict[str, int]:
        try:
            return {
                "preferencial": self._sillas_preferencial,
                "economica": self._sillas_economica
            }
        except Exception:
            self._mostrar_error()
            return {}

    def reservar_sillas(self, tipo: str, cantidad: int) -> bool:
        try:
            if tipo == "preferencial" and self._sillas_preferencial >= cantidad:
                self._sillas_preferencial -= cantidad
                return True
            elif tipo == "economica" and self._sillas_economica >= cantidad:
                self._sillas_economica -= cantidad
                return True
            return False
        except Exception:
            self._mostrar_error()
            return False

    def _mostrar_error(self):
        if 'tk' in globals():
            messagebox.showerror("Error", "Ha ocurrido un error, lo sentimos")
        else:
            print("Ha ocurrido un error, lo sentimos")
