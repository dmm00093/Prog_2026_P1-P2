# Libreria: (Clase: Habitacion) Control y parametrización de una habitación
# Autor: dmm00093@red.ujaen.es
# Funcion: crear, modificar y consultar dispositivos en una habitación

from libs.dispositivo import Dispositivo
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

    def encender_dispositivo(self, dispositivo):

        if dispositivo in self.__dispositivos:
            dispositivo.encender() # lo hacemos asi porque si hacemos self.__dispositivo[dispositivo].encender(dispositivo)
                                   # da error, tendrá su sentido
        else:
            raise Exception("Error: dispositivo no existe.")

    def apagar_dispositivo(self, dispositivo):

        if dispositivo in self.__dispositivos:
            dispositivo.apagar()
        else:
            raise Exception("Error: dispositivo no existe.")

    def get_dispositivos(self):
        ''' Obtiene TODOS los dispositivos de la habitacion '''
        return self.__dispositivos

    def get_dispositivo(self, nom_disp):
        ''' Obtiene UN SOLO dispositivo de la habitacion '''
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
            raise TypeError("Error: nombre de fichero debe ser un string.")
        if nomFich == '':
            raise Exception("Error: no se especifica nombre del fichero.")

        '''
        txtCheck = list(nomFich)
        txtlen   = len(txtCheck)

        txtCheckDebug = list() # para debuggear si esta bien
        i = 1
        while i <= 4:
            txtCheckDebug.append(txtCheck[txtlen - i])
            i+=1

        if txtCheck[txtlen-1] != 't' and txtCheck[txtlen-2] != 'x' and txtCheck[txtlen-3] != 't' and txtCheck[txtlen-4] != '.':
        '''

        if not nomFich.lower().endswith('.txt'): # esto al parecer lo hace directamente. dejo lo anterior comentado igual.
            raise Exception("Error: formato no correcto. Debe guardarse como un fichero de extensión <.txt>")

        sys_fecha_hora = str(Programador.getFechayHoraSistema()) # obtenemos hora local pc

        with open(nomFich, 'at', encoding='utf-8') as fichero: #utf8 por las tildes

            fichero.write(f"Fecha de escritura: [{sys_fecha_hora}]\nHabitación: {self.__nombre}\n")

            if len(self.__dispositivos) == 0:
                fichero.write("\n[*] Habitación sin dispositivos.\n")
            else:
                for disp in self.__dispositivos:

                    fichero.write(f"[*] {disp.consultar_params_texto_sinANSI()}")
                    fichero.write("------------------------------------------\n")