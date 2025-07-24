from Usuario import Usuario
from Cliente import Cliente 
from Administrador import Administrador
from Pasajero import Pasajero
from Vuelo import Vuelo
from Reserva import Reserva
from typing import List
import os

class Sistema:
    def _init_(self):
        self._clientes: List[Cliente] = []
        self._administradores: List[Administrador] = []
        self._vuelos: List[Vuelo] = []
        self._reservas: List[Reserva] = []

    def registrar_cliente(self, nombre, correo, id_cliente, contrasena):
        for cliente in self._clientes:
            if cliente.get_id() == id_cliente:
                return False # El cliente ya existe
        nuevo_cliente = Cliente(nombre, correo, id_cliente, contrasena)
        self._clientes.append(nuevo_cliente)
        return True

    def iniciar_sesion(self, id_usuario: str, contrasena: str) -> Usuario:
        for u in self._clientes + self._administradores:
            if u.get_id() == id_usuario and u.verificar_contrasena(contrasena):
                return u
        return None

    def agregar_vuelo(self, vuelo: Vuelo):
        self._vuelos.append(vuelo)

    def buscar_vuelos(self, origen: str, destino: str) -> List[Vuelo]:
        return [v for v in self._vuelos if v._origen == origen and v._destino == destino]

    def cargar_datos(self):
        if os.path.exists("clientes.txt"):
            with open("clientes.txt", "r") as f:
                for linea in f:
                    nombre, correo, id_cliente, contrasena, millas = linea.strip().split(",")
                    self._clientes.append(Cliente(nombre, correo, id_cliente, contrasena, int(millas)))
        
        if os.path.exists("vuelos.txt"):
            with open("vuelos.txt", "r") as f:
                for linea in f:
                    codigo, origen, destino, horario, sp, se = linea.strip().split("\t") # Usamos tab como separador
                    self._vuelos.append(Vuelo(codigo, origen, destino, horario, int(sp), int(se)))

    def guardar_datos(self):
        with open("clientes.txt", "w") as f:
            for c in self._clientes:
                f.write(f"{c.get_nombre()},{c.get_correo()},{c.get_id()},{c.get_contrasena()},{c.get_millas()}\n")
