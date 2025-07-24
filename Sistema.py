from Usuario import Usuario
from Cliente import Cliente 
from Administrador import Administrador
from Pasajero import Pasajero
from Vuelo import Vuelo
from Reserva import Reserva
from typing import List, Dict
import os
import tkinter as tk
from tkinter import messagebox


class Sistema:
    def __init__(self):
        self._clientes: List[Cliente] = []
        self._administradores: List[Administrador] = []
        self._vuelos: List[Vuelo] = []
        self._reservas: List[Reserva] = []

    def registrar_cliente(self, cliente: Cliente):
        try:
            self._clientes.append(cliente)
        except Exception:
            self._mostrar_error()

    def registrar_administrador(self, administrador: Administrador):
        try:
            self._administradores.append(administrador)
        except Exception:
            self._mostrar_error()

    def iniciar_sesion(self, documento: str, contrasena: str) -> Usuario:
        try:
            for u in self._clientes + self._administradores:
                if u._documento == documento and u._contrasena == contrasena:
                    return u
            return None
        except Exception:
            self._mostrar_error()
            return None

    def agregar_vuelo(self, vuelo: Vuelo):
        try:
            self._vuelos.append(vuelo)
        except Exception:
            self._mostrar_error()

    def buscar_vuelos(self, origen: str, destino: str) -> List[Vuelo]:
        try:
            return [v for v in self._vuelos if v._origen == origen or v._destino == destino]
        except Exception:
            self._mostrar_error()
            return []

    def realizar_reserva(self, cliente_doc: str, vuelo_cod: str, pasajeros: List[Pasajero]) -> Reserva:
        try:
            numero_reserva = f"R{len(self._reservas)+1:05d}"
            reserva = Reserva(numero_reserva, cliente_doc, vuelo_cod, pasajeros)
            self._reservas.append(reserva)
            for cliente in self._clientes:
                if cliente._documento == cliente_doc:
                    cliente._millas += 500
            return reserva
        except Exception:
            self._mostrar_error()
            return None

    def obtener_millas(self, documento: str) -> int:
        try:
            for cliente in self._clientes:
                if cliente._documento == documento:
                    return cliente._millas
            return 0
        except Exception:
            self._mostrar_error()
            return 0

    def cargar_datos(self):
        try:
            if os.path.exists("clientes.txt"):
                with open("clientes.txt", "r") as f:
                    for linea in f:
                        nombre, correo, documento, contrasena, millas = linea.strip().split(",")
                        self._clientes.append(Cliente(nombre, correo, documento, contrasena, int(millas)))

            if os.path.exists("vuelos.txt"):
                with open("vuelos.txt", "r") as f:
                    for linea in f:
                        codigo, origen, destino, horario, sp, se = linea.strip().split(",")
                        self._vuelos.append(Vuelo(codigo, origen, destino, horario, int(sp), int(se)))
        except Exception:
            self._mostrar_error()

    def guardar_datos(self):
        try:
            with open("clientes.txt", "w") as f:
                for c in self._clientes:
                    f.write(f"{c._nombre},{c._correo},{c._documento},{c._contrasena},{c._millas}\n")

            with open("vuelos.txt", "w") as f:
                for v in self._vuelos:
                    f.write(f"{v._codigo},{v._origen},{v._destino},{v._horario},{v._sillas_preferencial},{v._sillas_economica}\n")
        except Exception:
            self._mostrar_error()

    def _mostrar_error(self):
        if 'tk' in globals():
            messagebox.showerror("Error", "Ha ocurrido un error, lo sentimos")
        else:
            print("Ha ocurrido un error, lo sentimos")
