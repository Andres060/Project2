class Reserva():
    def __init__(self, numReserva, cliente, vuelo, pasajeros, total, checkInRealizado, millasAcumuladas, equipaje):
        self.__numReserva = numReserva
        self.__cliente = cliente
        self.__vuelo = vuelo
        self.__pasajeros = pasajeros
        self.__total = total
        self.__checkInRealizado = checkInRealizado
        self.__millasAcumuladas = millasAcumuladas
        self.__equipaje = equipaje

    def calcularTotal(self):
        pass

    def modificar(self):
        pass

    def cancelar(self):
        pass

    def realizarCheckIn(self):
        pass

    def toString(self):
        pass