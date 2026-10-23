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
from libs.ansi_colores import color


class AC:

    def __init__(self, nombre, descripcion, tamb=25):  # asume 25ºC si no se especifica

        self.__tamb = tamb
        self.__temp = 22
        self.__fuerza = 50
        self.__estado = False
        self.__ahorro = False
        self.__descripcion = descripcion
        self.__nombre = nombre

    def set_tamb(self, tamb2):

        self.__tamb = tamb2
        return 0

    def get_tamb(self):

        return self.__tamb

    def set_temp(self, temp):

        if temp < 10 or temp > 30: # Temperaturas límite de la máquina

            self.__temp = 21
            return -1 # ERROR = 1 asigna valor por defecto

        else:

            self.__temp = temp
            return 0 # valido

    def get_temp(self):

        return self.__temp

    def set_fuerza(self, fuerza):

        if fuerza <= 0 or fuerza > 100:

            self.__fuerza = 50
            return -1 # ERROR = 1 asigna valor por defecto, mayor que 100 o menor que 0

        else:

            self.__fuerza = fuerza
            return 0 # valido

    def get_fuerza(self):

        return self.__fuerza

    def set_estado(self, estado):

        self.__estado = estado
        return 0

    def get_estado(self):

        return self.__estado

    def set_ahorro(self, ahorro):

        self.__ahorro = ahorro
        return 0

    def get_ahorro(self):

        return self.__ahorro

    def set_descripcion(self, descripcion):

        self.__descripcion = descripcion
        return 0

    def get_descripcion(self):

        return self.__descripcion

    def set_nombre(self, nombre2):

        self.__nombre = nombre2
        return 0

    def get_nombre(self):

        return self.__nombre

    def consultar_params_texto(self):

        # funcion EXPLICITAMENTE para devolver TEXTO POR PANTALLA.
        # uso un string (texto) que le haremos un return para mostrar por pantalla
        # cada vez vamos añadiendo cosas. en vez de usar prints, ya que no se deben incluir prints
        # basicamente, cambiamos la estructura de print(...), print(...) por texto = (...), texto = texto + (...), y asi

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

        texto = color.AZUL + color.NEGRITA + "Parámetros de " + str(self.__nombre) + " : " + color.RESET + "\n"

        texto += "Temperatura ambiente (ºC): " + str(self.__tamb) + " \nTemperatura programada (ºC): " + str(
            self.__temp) + " \nFuerza (%): " + str(self.__fuerza) + " \nEstado: " + str(
            display) + " \n¿Modo ahorro activo?: " + str(display2) + " \nDescripcion: " + str(self.__descripcion)

        return texto

