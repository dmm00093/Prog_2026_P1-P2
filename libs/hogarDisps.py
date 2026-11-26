# Libreria: (Clase: Hogar) Control y parametrización de dispositivos en un hogar y sus localizaciones
# Autor: dmm00093@red.ujaen.es
# Funcion: crear, modificar y consultar dispositivos y habitaciones en un hogar
# Funcionalidades:
"""
    - Conocer todos los parámetros de los dispositivos de un hogar
    - Conocer todas las habitaciones de un hogar
    - Modificar todos los parámetros (parámetros, dispositivos y habitaciones) del hogar
"""

from libs.ansi_colores import Color
from libs.habitacion import Habitacion

class Hogar:

    def __init__ (self):
        self.__habitaciones = {} # diccionario vacio

    def crear_habitacion (self, nombre_hab):

        if nombre_hab not in self.__habitaciones:
            self.__habitaciones[nombre_hab] = Habitacion(nombre_hab) # Si no existe, creamos la habitacion.

        else:
            raise Exception("Ya existe la habitación") # ERR = 1, no existe la habitacion

    def add_dispositivo (self, nombre_hab, dispositivo):

        if nombre_hab in self.__habitaciones:
            self.__habitaciones[nombre_hab].add_dispositivo(dispositivo) # Si existe la habitacion, añadimos dispositivo

        else:
            raise Exception("No existe la habitación")


    def quitar_dispositivo (self, nombre_hab, dispositivo):

        if nombre_hab in self.__habitaciones:
            self.__habitaciones[nombre_hab].quitar_dispositivo(dispositivo) # Si existe la habitacion, eliminamos

        else:
            raise Exception("No existe la habitación") # ERR = 1, no existe la habitacion

    def mover_dispositivo (self, nombre_hab, nombre_hab2, dispositivo):

        if nombre_hab in self.__habitaciones and nombre_hab2 in self.__habitaciones:

            # Si existe la habitacion1 y habitacion2 en el diccionario, podemos seguir
            self.__habitaciones[nombre_hab].quitar_dispositivo(dispositivo)
            self.__habitaciones[nombre_hab2].add_dispositivo(dispositivo)

        else:
            raise Exception("No existe la habitación") # ERR = 1, no existe la habitacion

    def encender_dispositivo (self, nombre_hab, dispositivo):

        if nombre_hab in self.__habitaciones: # Existe la habitacion?
            self.__habitaciones[nombre_hab].encender_dispositivo(dispositivo)

        else:
            raise Exception("No existe la habitación") # error, no existe habitacion

    def apagar_dispositivo(self, nombre_hab, dispositivo):

        if nombre_hab in self.__habitaciones: # Igual que def encender_dispositivo
            self.__habitaciones[nombre_hab].apagar_dispositivo(dispositivo)

        else:
            raise Exception("No existe la habitación") # error, no existe habitacion

    def mostrar_hogar_texto(self):

        """
        Funcion EXPLICITAMENTE para devolver TEXTO POR PANTALLA.
        Crea y devuelve un STRING con todos los parametros que muestra por texto en pantalla.
        Modificada a fstring 20/11 para tener un estandar en todas las librerias
        """

        texto = f"{Color.AZUL.value}\nMostrando habitaciones y dispositivos:\n{Color.RESET.value}\n"

        for hab, habitacion_obj in self.__habitaciones.items():
            texto += f"Habitación {Color.AMARILLO.value}{Color.NEGRITA.value}{hab} :\n{Color.RESET.value}\n"

            lista_disps = habitacion_obj.get_dispositivos()

            if len(lista_disps) == 0:
                texto += f"{Color.ROJO.value}{Color.NEGRITA.value} [*] Habitación vacía {Color.RESET.value}\n"

            for disp in lista_disps:
                texto += f"{Color.VERDE.value}{Color.NEGRITA.value} [*] "
                texto += disp.consultar_params_texto()
                texto += f"{Color.AZUL.value}{Color.NEGRITA.value}\n"
                texto += f"------------------------------------\n {Color.RESET.value}\n"

        return texto


    def mostrar_hogar_texto_sinANSI(self):

        texto = "\nMostrando habitaciones y dispositivos:\n"

        for hab, habitacion_obj in self.__habitaciones.items():
            texto += f"Habitación {hab}:\n"

            lista_disps = habitacion_obj.get_dispositivos()

            if len(lista_disps) == 0:
                texto += f"[*] Habitación vacía\n"

            for disp in lista_disps:
                texto += f"[*]"
                texto += disp.consultar_params_texto_sinANSI()
                texto += f"\n"
                texto += f"------------------------------------\n"

        return texto

    def guardar_log_habitacion(self, nombre_hab, nomFich):
        ''' Guarda el log de la habitación especificada '''
        if nombre_hab in self.__habitaciones:
            self.__habitaciones[nombre_hab].guardaLog(nomFich)
        else:
            raise Exception("Error: No existe la habitación")