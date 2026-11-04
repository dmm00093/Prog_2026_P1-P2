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
                 nombreLed = '', nivelIntensidad = 0, maxIntensidad = 1, minIntensidad = 0, estadoLed = False,
                 tamb = 25, temp = 20, fuerza = 50, estadoAC = False, ahorro = False, descripcion = '',
                 nombre = ''):

        self.__nombreLed = nombreLed
        self.__nivelIntensidad = nivelIntensidad
        self.__maxIntensidad = maxIntensidad
        self.__minIntensidad = minIntensidad
        self.__estadoLed = estadoLed
        self.__tamb = tamb
        self.__temp = temp
        self.__fuerza = fuerza
        self.__estadoAC = estadoAC
        self.__ahorro = ahorro
        self.__descripcion = descripcion
        self.__nombre = nombre

