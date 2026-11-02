# clase: programador
# listaprogramacion : list()
# idprogramador : strng
# contador = 0

# getDiasSemana() : list()
# getHoraSistema() : String
# comienzo(diaSemana : string, hora:byte, min:byte, seg:byte)
# fin(diaSemana : string, hora:byte, min:byte, seg:byte)
# borrar(diaSemana : string, hora:byte, min:byte, seg:byte)
# getProgramacion() : list(), devolverá la programación de esa bombilla

# Esta clase tendrá varios métodos de clase:
#Un métod que devolverá una lista con los nombres válidos de los días de la semana
# (para saber que nombre se pueden usar para programar el programador).
#Un métod que devolverá la hora actual del sistema.
# Usará el formato : DiaDeLaSemana hora:minutos:segundos (*).

'''
(*) Para calcular la hora del sistema se podrá usar :

import time

print(time.localtime() )

time.localtime() devuelve un objeto (struc_time) con los siguientes campos :
tm_year=2021, tm_mon=8, tm_mday=3, tm_hour=16, tm_min=15, tm_sec=8, tm_wday=1,
tm_yday=215, tm_isdst=0
(nota, los valores asignados son ejemplos)
'''

import time

class Programador:

    cont = 0

    def __init__(self, bombilla):

        self.__bombilla = bombilla
        self.__listaprogramacion = []

        self.__idProgramador = "Programador" + str(Programador.cont)
        Programador.cont += 1

    def getDiasSemana(self):

        # esto es una lista, pero no hacemos prints
        diasSemana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        return diasSemana

    def getHoraSistema(self):

        # esto tambien es un parámetro que no printeamos, devolvemos.
        tiempo = time.localtime()
        dias = self.getDiasSemana()
        dia_actual = dias[tiempo.tm_wday] # tm_wday va de 0 a 6, lunes a dom.

        sys_tiempo = [dia_actual, tiempo.tm_hour, tiempo.tm_min, tiempo.tm_sec]

        return sys_tiempo

    def comienzo(self, diaSemana, hora, min, seg):

        # creacion de esa actualizacion en programacion y la añadimos.
        actualizacion = ["Comienzo: {Día:,", diaSemana, ", Hora:", hora, ", Minuto:", min, ", Segundo:", seg, "}"]
        self.__listaprogramacion.append(actualizacion)

    def fin(self, diaSemana, hora, min, seg):

        # creacion de esa actualizacion en programacion y la añadimos.
        actualizacion = ["Comienzo: {Día:,", diaSemana, ", Hora:", hora, ", Minuto:", min, ", Segundo:", seg, "}"]
        self.__listaprogramacion.append(actualizacion)


