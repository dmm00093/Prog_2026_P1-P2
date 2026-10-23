# Libreria: (Clase: Hogar) Control y parametrización de dispositivos en un hogar y sus localizaciones
# Autor: dmm00093@red.ujaen.es
# Funcion: crear, modificar y consultar dispositivos y habitaciones en un hogar
# Funcionalidades:
"""
    - Conocer todos los parámetros de los dispositivos de un hogar
    - Conocer todas las habitaciones de un hogar
    - Modificar todos los parámetros (parámetros, dispositivos y habitaciones) del hogar
"""

from libs.ansi_colores import color

class Hogar:

    def __init__ (self):

        self.__habitaciones = {} # diccionario vacio

    def crear_habitacion (self, nombre_hab):

        if nombre_hab not in self.__habitaciones:

            self.__habitaciones[nombre_hab] = [] # Si no existe, creamos la habitacion.
            return 0 # valido

        else:
            return -1 # ERR = 1, no existe la habitacion

    def add_dispositivo (self, nombre_hab, dispositivo):

        if nombre_hab in self.__habitaciones:

            self.__habitaciones[nombre_hab].append(dispositivo) # Si existe la habitacion, añadimos dispositivo
            return 0 # valido

        else:
            return -1 # ERR = 1, no existe la habitacion

    def quitar_dispositivo (self, nombre_hab, dispositivo):

        if nombre_hab in self.__habitaciones:

            self.__habitaciones[nombre_hab].remove(dispositivo) # Si existe la habitacion, eliminamos
            return 0 # valido

        else:
            return -1 # ERR = 1, no existe la habitacion

    def mover_dispositivo (self, nombre_hab, nombre_hab2, dispositivo):

        if nombre_hab in self.__habitaciones and nombre_hab2 in self.__habitaciones:

            # Si existe la habitacion1 y habitacion2 en el diccionario, podemos seguir

            self.__habitaciones[nombre_hab].remove(dispositivo)
            self.__habitaciones[nombre_hab2].append(dispositivo)

            return 0 # valido

        else:
            return -1 # ERR = 1, no existe la habitacion

    def encender_dispositivo (self, nombre_hab, dispositivo):

        if nombre_hab in self.__habitaciones: # Existe la habitacion?

            lista_disps = self.__habitaciones[nombre_hab] # Lista con los valores de esa habitacion.

            for disp in lista_disps: # Por cada dispositivo en esa lista...

                if disp == dispositivo: # Si el dispositivo coincide con el input...

                    dispositivo.set_estado(True) # Encendemos
                    return 0 # valido

        else:
            return -1 # error, no existe habitacion

    def apagar_dispositivo(self, nombre_hab, dispositivo):

        if nombre_hab in self.__habitaciones: # Igual que def apagar_dispositivo

            lista_disps = self.__habitaciones[nombre_hab]

            for disp in lista_disps:

                if disp == dispositivo:
                    dispositivo.set_estado(False)
                    return 0
        else:
            return -1 # error, no existe habitacion

    def mostrar_hogar_texto(self):

        """
        Funcion EXPLICITAMENTE para devolver TEXTO POR PANTALLA.
        Crea y devuelve un STRING con todos los parametros que muestra por texto en pantalla.
        """

        # cada vez vamos añadiendo cosas. en vez de usar prints, ya que no se deben incluir prints
        # basicamente, cambiamos la estructura de print(...), print(...) por texto = (...), texto = texto + (...), y asi

        # TODO: Arreglar espacios al usar los valores ansi y eliminar tantos espacios
        # mas o menos hecho pero no se como terminar de arreglarlo

        texto = color.AZUL + "\nMostrando habitaciones y dispositivos:\n" + color.RESET + "\n"

        for hab, dispositivos in self.__habitaciones.items():  # recorremos cada habitacion del diccionario

            texto += "Habitación " + color.AMARILLO + color.NEGRITA + str(hab) + " :\n" + color.RESET + "\n"

            if self.__habitaciones[hab] == []:
                texto += color.ROJO + color.NEGRITA + " [*] Habitación vacía " + color.RESET + "\n"

            for disp in dispositivos:  # por cada habitacion mostramos la lista de dispositivos

                texto += color.VERDE + color.NEGRITA + " [*] "
                texto += disp.consultar_params_texto()  # como la funcion se llama igual en todos, viene de lujo.

                texto += color.AZUL + color.NEGRITA + "\n"
                texto += "------------------------------------\n " + color.RESET + "\n"

        return texto