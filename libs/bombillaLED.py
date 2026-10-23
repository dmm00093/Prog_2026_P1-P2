# Libreria: bombilla
# Funcion: crear, modificar y consultar parámetros de una bombilla
# Funcionalidades:
"""
    - Conocer todos los parámetros de la bombilla
    - Modificar todos los parámetros de la bombilla
"""
from libs.ansi_colores import color


class Bombilla:

    def __init__(self, nombre, descripcion):

        self.__estado = False
        self.__color = [255, 255, 255]
        self.__intensidad = 200
        self.__nivelblanco = 2
        self.__descripcion = descripcion
        self.__nombre = nombre

    def set_estado(self, estado):

        self.__estado = estado
        return 0

    def get_estado(self):

        return self.__estado

    def set_intensidad(self, intensidad):

        if intensidad == 0:

            self.__estado = False # Si intensidad = 0 apagamos
            return 0 # valido

        elif intensidad > 255:

            self.__intensidad = 255
            return -1 # ERROR = 1, mayor que 255, asigna 255 por defecto

        else:

            self.__intensidad = intensidad
            return 0 # valido

    def get_intensidad(self):

        return self.__intensidad

    def set_color(self, R, G, B):

        colorNuevo = [R, G, B]
        errcod = 0

        i = 0
        listaColoresError = ["R", "G", "B"]

        while (i < len(listaColoresError)): # Comparación de listas

            if colorNuevo[i] > 255:

                colorNuevo[i] = 255
                errcod = -1

            i += 1

        self.__color = colorNuevo
        return errcod # válido = 0, hubo error (valos defecto) = -1

    def get_color(self):

        return self.__color

    def set_nivelblanco(self, nivelblanco):

        if 1 > nivelblanco or nivelblanco > 3:

            self.__nivelblanco = 1
            return -1 # ERROR = 1 asigna valor por defecto

        else:

            self.__nivelblanco = nivelblanco
            return 0 # valido

    def get_nivelblanco(self):

        return self.__nivelblanco

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

        # def consultar_params_texto -> mismo nombre en todos los dispositivos
        # facilita mostrar información en hogar

        if self.__estado == True:
            display = "ON"
        else:
            display = "OFF"

        print(color.RESET, "Parámetros de", self.__nombre, ":")
        print(f"Estado:", display, "\nColor:", self.__color, "\nIntensidad:", self.__intensidad,
              "\nNivel de Blanco:", self.__nivelblanco, "\nDescripcion:", self.__descripcion)
