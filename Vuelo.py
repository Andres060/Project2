class Vuelo():
    def __init__(self, codigo, origen, destino, horario, sillasPreferencial, sillasEconomica, reservas):
        self.__codigo = codigo
        self.__origen = origen
        self.__destino = destino
        self.__horario = horario
        self.__sillasPreferencial = sillasPreferencial
        self.__sillasEconomica = sillasEconomica
        self.__reservas = reservas

    def disponibilidad(self):
        pass

    def reservarSillas(self, tipo, cantidad):
        pass

    def toString(self):
        pass
    