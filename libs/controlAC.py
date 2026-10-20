# Libreria: Control Aire Acondicionado (controlAC)
# Funcion: Gestion de AC
# Funcionalidades:
"""
    - Conocer la temperatura ambiente.
    - Poder cambiar la temperatura del aire acondicionado.
    - Poder cambiar la fuerza del aire.
    - Conocer si está apagado o encendido.
    - Debemos poder apagarlo y encenderlo.
    - Pueda activar/desactivar el modo ahorro energético (tecnología inverter).
    - Pueda obtener una descripción del dispositivo (marca, modelo, etc.).
"""

class AC:

    def __init__(self, nombre, descripcion, tamb=25):  # asume 25ºC si no se especifica

        self.__tamb = tamb
        self.__temp = 22
        self.__fuerza = 50
        self.__estado = False
        self.__ahorro = False
        self.__descripcion = descripcion
        self.__nombre = nombre

    def cambiar_temp(self, temp):

        if temp < 10 or temp > 30: # Temperaturas límite de la máquina

            self.__temp = 21
            return -1 # ERROR = 1 asigna valor por defecto

        else:

            self.__temp = temp
            return 0 # valido

    def cambiar_fuerza(self, fuerza):

        if fuerza <= 0 or fuerza > 100:

            self.__fuerza = 50
            return -1 # ERROR = 1 asigna valor por defecto, mayor que 100 o menor que 0

        else:

            self.__fuerza = fuerza
            return 0 # valido

    def cambiar_estado(self, estado):

        self.__estado = estado

    def cambiar_modo_ahorro(self, ahorro):

        self.__ahorro = ahorro

    def cambiar_descripcion(self, descripcion):

        self.__descripcion = descripcion

    def consultar_params_texto(self):

        # def consultar_params_texto -> mismo nombre en todos los dispositivos
        # facilita mostrar informacion en hogar

        if self.__estado:
            display = "ON"
        else:
            display = "OFF"

        if self.__ahorro:
            display2 = "ON"
        else:
            display2 = "OFF"

        print("Parámetros de", self.__nombre, ":")

        print("Temperatura ambiente (ºC):", self.__tamb, "\nTemperatura programada (ºC):", self.__temp,
              "\nFuerza (%):", self.__fuerza, "\nEstado:", display, "\n¿Modo ahorro activo?:", display2,
              "\nDescripcion:", self.__descripcion)

