'''
a) Vamos a crear una nueva clase Dispositivo que agrupará todas las características comunes que tienen los dispositivos
que podemos controlar con el HUB, tanto atributos como métodos. Como mínimo incluiremos los métodos encender, apagar,
disminuirIntensidad, aumentarIntensidad.

Clase dispositivo

b) Queremos realizar una gestión de errores en el caso de que disminuirIntensidad y aumentarIntensidad superen el
umbral previsto por el dispositivo. En el caso de que esto ocurra, los métodos lanzarán (raise) un error de tipo
ValueError con un mensaje de error explicando la causa.

c) En el programa principal queremos que se capture dicho error y se gestione correctamente, es decir,
se le vuelva a preguntar al usuario que que quiere hacer.
'''

#TODO: TODO ESTA MAL!!!!!! APLICAR HERENCIAS CON AC Y BOMBILLA, METODOS Y ATRIBUTOS REDUNDANTES!

class Dispositivo:

    def __init__(self,
                 nombre = '', nivelIntensidad = 0, maxIntensidad = 1, minIntensidad = 0, color=None,
                 nivelblanco = 1, estado = False, descripcion = '', tamb = 25, temp = 20,
                 fuerza = 50, ahorro = False):

        # --- atributos GENÉRICOS --- #
        self.__nombre = nombre
        self.__estado = estado
        self.__descripcion = descripcion
        # --- atributos BOMBILLA --- #
        if color is None:
            color = [255, 255, 255]
        self.__color = color
        self.__nivelIntensidad = nivelIntensidad
        self.__maxIntensidad = maxIntensidad
        self.__minIntensidad = minIntensidad
        self.__nivelblanco = nivelblanco
        # --- atributos AC --- #
        self.__tamb = tamb
        self.__temp = temp
        self.__fuerza = fuerza
        self.__ahorro = ahorro

    # --- Métodos get --- #

    # --- Get genéricos --- #
    def get_nombre(self):
        return self.__nombre

    def get_estado(self):
        return self.__estado

    def get_descripcion(self):
        return self.__descripcion

    # --- Get bombilla --- #
    def get_color(self):
        return self.__color

    def get_nivelIntensidad(self):
        return self.__nivelIntensidad

    def get_maxIntensidad(self):
        return self.__maxIntensidad

    def get_minIntensidad(self):
        return self.__minIntensidad

    def get_nivelblanco(self):
        return self.__nivelblanco

    # --- Get AC --- #

    def get_tamb(self):
        return self.__tamb

    def get_temp(self):
        return self.__temp

    def get_fuerza(self):
        return self.__fuerza

    def get_ahorro(self):
        return self.__ahorro

    # --- Metodos genéricos --- #

    def set_nombre(self, nombre2):

        if not isinstance(nombre2, str):
            raise TypeError("ERROR: nombre debe ser un string.")
        self.__nombre = nombre2

    def encender(self):

        if self.__estado == True:
            raise Exception("ERROR: dispositivo ya encendido.")
        self.__estado = True

    def apagar(self):

        if self.__estado == False:
            raise Exception("ERROR: dispositivo ya apagado.")
        self.__estado = False

    def set_descripcion(self, descripcion2):

        if not isinstance(descripcion2, str):
            raise TypeError("ERROR: descripción debe ser un string.")
        self.__descripcion = descripcion2

    # --- Métodos BOMBILLA --- #

    def set_color(self, R2, G2, B2):

        listaRGB_2 = [R2, G2, B2]

        for param in listaRGB_2:

            if param < 0 or param > 255:

                raise ValueError(f"ERROR: el color {param} tiene un valor erróneo. Especificar entre 0 y 255.")
                # finalmente he cedido y uso esto de los fstring... no me gustan pero es mas limpio

        self.__color = listaRGB_2

    def set_nivelIntensidad(self, intensidad2):

        if intensidad2 < 0 or intensidad2 > 255:
            raise ValueError("ERROR: intensidad fuera de los límites (0 min, 255 max)")

        self.__nivelIntensidad = intensidad2

    def disminuirIntensidad(self, decremento):

        intensidadFinal = self.__nivelIntensidad - decremento

        if intensidadFinal < self.__minIntensidad:
            raise ValueError("La intensidad no puede ser menor que el umbral mínimo.")

        self.__nivelIntensidad = intensidadFinal

    def aumentarIntensidad(self, incremento):

        intensidadFinal = self.__nivelIntensidad + incremento

        if intensidadFinal > self.__maxIntensidad:
            raise ValueError("La intensidad no puede ser mayor que el umbral máximo.")

        self.__nivelIntensidad = intensidadFinal

    def set_nivelblanco(self, nivelblanco2):

        if 0 > nivelblanco2 or nivelblanco2 > 3:

            raise ValueError("ERROR: nivel de blanco fuera de los límites (0 min, 3 max)")

        self.__nivelblanco = nivelblanco2

    # --- Métodos AC --- #

    def set_tamb(self, tamb2):

        if -50 > tamb2 or tamb2 > 50:

            raise ValueError("ERROR: temperatura ambiente fuera de rango (-50, +50)")

        self.__tamb = tamb2

    def set_temp(self, temp2):

        if 0 > temp2 or temp2 > 35:
            raise ValueError("ERROR: temperatura fuera de rango (0, 35)")

        self.__temp = temp2

    def set_fuerza(self, fuerza2):

        if 0 > fuerza2 or fuerza2 > 100:
            raise ValueError("ERROR: fuerza fuera de rango (0, 100)")

        self.__fuerza = fuerza2

    def encenderAhorro(self):

        if self.__ahorro == True:
            raise Exception("ERROR: modo ahorro ya encendido.")
        self.__ahorro = True

    def apagarAhorro(self):

        if self.__ahorro == False:
            raise Exception("ERROR: modo ahorro ya apagado.")
        self.__ahorro = False

