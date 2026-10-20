# Libreria: bombilla
# Funcion: crear, modificar y consultar parámetros de una bombilla
# Funcionalidades:
"""
    - Conocer todos los parámetros de la bombilla
    - Modificar todos los parámetros de la bombilla
"""

class Bombilla:

    def __init__(self, nombre, descripcion):

        self.__estado = False
        self.__color = [255, 255, 255]
        self.__intensidad = 200
        self.__nivelblanco = 2
        self.__descripcion = descripcion
        self.__nombre = nombre

    def cambiar_estado(self, estado):

        self.__estado = estado

    def cambiar_intensidad(self, intensidad):

        if intensidad == 0:

            self.__estado = False # Si intensidad = 0 apagamos
            return 0 # valido

        elif intensidad > 255:

            self.__intensidad = 255
            return -1 # ERROR = 1, mayor que 255, asigna 255 por defecto

        else:

            self.__intensidad = intensidad
            return 0 # valido

    def cambiar_color(self, R, G, B):

        colorNuevo = [R, G, B]

        i = 0
        listaColoresError = ["R", "G", "B"]

        while (i < len(listaColoresError)): # Comparación de listas

            if colorNuevo[i] > 255:

                colorNuevo[i] = 255
                return -1 # ERROR = 1 asigna valor por defecto

            i += 1

        self.__color = colorNuevo
        return 0 # válido

    def cambiar_nivel_blanco(self, nivelblanco):

        if 1 > nivelblanco or nivelblanco > 3:

            self.__nivelblanco = 1
            return -1 # ERROR = 1 asigna valor por defecto

        else:

            self.__nivelblanco = nivelblanco
            return 0 # valido

    def cambiar_descripcion(self, descripcion):

        self.__descripcion = descripcion

    def consultar_params_texto(self):

        # def consultar_params_texto -> mismo nombre en todos los dispositivos
        # facilita mostrar informacion en hogar

        if self.__estado == True:
            display = "ON"
        else:
            display = "OFF"

        print("Parámetros de", self.__nombre, ":")
        print(f"Estado:", display, "\nColor:", self.__color, "\nIntensidad:", self.__intensidad,
              "\nNivel de Blanco:", self.__nivelblanco, "\nDescripcion:", self.__descripcion)
