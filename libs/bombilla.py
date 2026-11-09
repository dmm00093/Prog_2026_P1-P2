# Libreria: (Clase: Bombilla) Control y parametrizacion de una Bombilla
# Autor: dmm00093@red.ujaen.es
# Funcion: crear, modificar y consultar parámetros de una bombilla
# Funcionalidades:
"""
    - Conocer todos los parámetros de la bombilla
    - Modificar todos los parámetros de la bombilla
"""

from libs.ansi_colores import Color
from libs.dispositivo import Dispositivo

class Bombilla(Dispositivo):

    __cont = 0 # creacion de un contador genérico privado

    def __init__(self, nombre, descripcion, intensidad=200, estado=False, color=None, nivelblanco=2):

        # Herencia bombilla de dispositivo
        super().__init__(nombre=nombre, descripcion = descripcion, estado = estado, nivelIntensidad = intensidad)

        # creacion de atributo contador para tener nuestra lista de bombillas enumerada.
        self.__idbombilla = "Bombilla" + str(Bombilla.__cont)
        Bombilla.__cont += 1

        # atributos Bombilla propios
        if color is None: # sugerido por editor, ahorro de dolor de cabeza
            color = [255, 255, 255]
        self.__color = color
        self.__nivelblanco = nivelblanco

    def get_idBombilla(self): # hemos metido otro nuevo atributo a la clase, nuevo get.

        return self.__idbombilla

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

    def consultar_params_texto(self):

        """
        Funcion EXPLICITAMENTE para devolver TEXTO POR PANTALLA.
        Crea y devuelve un STRING con todos los parametros que muestra por texto en pantalla.
        """

        # formato -> fstrings, no me gustan pero quedan muy bien, más vistoso. antes era imposible de ampliar.
        # def consultar_params_texto -> mismo nombre en todos los dispositivos
        # facilita mostrar información en hogar

        if self.get_estado() == True:
            display = "ON"
        else:
            display = "OFF"

        # self.__intensidad cambia por self.get_nivelIntensidad() y __descripcion por get_descripcion()
        # igual que self.get_nombre() reemplaza a self.__nombre
        # esto es por la herencia de esta clase, que ya no tiene un metod nativo a si mismo que obtenga su nombre
        # sino que depende de la clase superior, en este caso, class Dispositivo.

        texto = (
            f"{Color.RESET.value}{Color.AZUL.value}{Color.NEGRITA.value}"
            f"Parámetros de {self.get_nombre()} :{Color.RESET.value}\n" # primer espacio de linea
            f"Estado: {display}\n" # 2o espacio
            f"Color: {self.__color}\n" # 3er espacio...
            f"Intensidad: {self.get_nivelIntensidad()}\n"
            f"Nivel de Blanco: {self.__nivelblanco}\n"
            f"Descripción: {self.get_descripcion()}\n"
        )

        return texto