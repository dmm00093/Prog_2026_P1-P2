from libs.interfaz import LogHistorico
from libs.programador import Programador

class Habitacion(LogHistorico):

    def __init__(self, nombre):

        super().__init__()
        self.__nombre = nombre
        self.__dispositivos = []

    def add_dispositivo(self, dispositivo):

        if dispositivo in self.__dispositivos:
            raise Exception("Error: dispositivo ya existe.")
        else:
            self.__dispositivos.append(dispositivo)

    def quitar_dispositivo(self, dispositivo):

        if dispositivo in self.__dispositivos:
            self.__dispositivos.remove(dispositivo)
        else:
            raise Exception("Error: dispositivo no existe.")

    def get_dispositivos(self):

        return self.__dispositivos

    def get_dispositivo(self, nom_disp):

        for disp in self.__dispositivos:
            if disp.get_nombre() == nom_disp:
                return disp

        return -1

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def guardaLog(self, nomFich):

        if not isinstance(nomFich, str):
            raise TypeError("ERROR: nombre de fichero debe ser un string.")

        sys_fecha_hora = Programador.getHoraSistema()

        with open(nomFich, 'at') as fichero:
            fichero.write(sys_fecha_hora)
            fichero.write(self.__dispositivos)


