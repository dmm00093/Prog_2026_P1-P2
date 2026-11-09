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

class Dispositivo:

    def __init__(self,
                 nombre = '', nivelIntensidad = 0, maxIntensidad = 1, minIntensidad = 0,
                 estado = False, descripcion = ''):

        # --- atributos GENÉRICOS --- #

        self.__nombre = nombre
        self.__estado = estado
        self.__descripcion = descripcion
        self.__nivelIntensidad = nivelIntensidad
        self.__maxIntensidad = maxIntensidad
        self.__minIntensidad = minIntensidad

    # --- Métodos get --- #

    # --- Get genéricos --- #

    def get_nombre(self):
        return self.__nombre

    def get_estado(self):
        return self.__estado

    def get_descripcion(self):
        return self.__descripcion

    def get_nivelIntensidad(self):
        return self.__nivelIntensidad

    def get_maxIntensidad(self):
        return self.__maxIntensidad

    def get_minIntensidad(self):
        return self.__minIntensidad

    # --- Metodos genéricos --- #

    def set_nombre(self, nombre2):

        if not isinstance(nombre2, str):
            raise TypeError("ERROR: nombre debe ser un string.")
        self.__nombre = nombre2

    def encender(self): # en teoría, encender y apagar son como set_estado, pero el UML pide los def ASÍ.

        if self.__estado == True:
            raise Exception("ERROR: dispositivo ya encendido.")
        self.__estado = True

    def apagar(self): # en teoría, encender y apagar son como set_estado, pero el UML pide los def ASÍ.

        if self.__estado == False:
            raise Exception("ERROR: dispositivo ya apagado.")
        self.__estado = False

    def set_descripcion(self, descripcion2):

        if not isinstance(descripcion2, str):
            raise TypeError("ERROR: descripción debe ser un string.")
        self.__descripcion = descripcion2

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
