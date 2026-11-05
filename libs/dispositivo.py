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

    def encender(self):

        self.__estado = True
        return 0

    def apagar(self):

        self.__estado = False
        return 0

    def disminuirIntensidad(self, decremento):

        intensidadFinal = self.__nivelIntensidad - decremento

        if intensidadFinal < self.__minIntensidad:

            raise ValueError("La intensidad no puede ser menor que el umbral mínimo.")

        else:

            self.__nivelIntensidad = intensidadFinal

        return 0

    def aumentarIntensidad(self, incremento):
        self.__nivelIntensidad = self.__nivelIntensidad - incremento
        return 0




