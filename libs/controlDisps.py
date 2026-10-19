from libs.bombillaLED import Bombilla
from libs.controlAC import AC
from libs.ansi_colores import color

# ToDo: mejorar estética y mensajes de confirmación + opcional: inputs (aunque eso mejor en main).

class Hogar:

    def __init__ (self):

        self.habitaciones = {} # diccionario vacio

    def crear_habitacion (self, nombre_hab):

        if nombre_hab not in self.habitaciones:

            self.habitaciones[nombre_hab] = []

        else:

            print("La habitación ya existe.")

    def add_dispositivo (self, nombre_hab, dispositivo):

        if nombre_hab in self.habitaciones:

            self.habitaciones[nombre_hab].append(dispositivo)
            print("Dispositivo agregado.")

        else:

            print("Error: no existe la habitación.")

    def quitar_dispositivo (self, nombre_hab, dispositivo):

        if nombre_hab in self.habitaciones:

            self.habitaciones[nombre_hab].remove(dispositivo)
            print("Dispositivo eliminado.")

        else:

            print("Error: no existe la habitación.")

    def mover_dispositivo (self, nombre_hab, nombre_hab2, dispositivo):

        if nombre_hab in self.habitaciones and nombre_hab2 in self.habitaciones:

            self.habitaciones[nombre_hab].remove(dispositivo)
            self.habitaciones[nombre_hab2].append(dispositivo)
            print("Dispositivo realojado.")

        else:

            print("Error: no existe la habitación.")

    def encender_dispositivo (self, nombre_hab, dispositivo):

        if nombre_hab in self.habitaciones:

            lista_disps = self.habitaciones[nombre_hab]

            for disp in lista_disps:

                if disp == dispositivo:

                    dispositivo.cambiar_estado(True)
                    print("Dispositivo encendido.")

    def apagar_dispositivo(self, nombre_hab, dispositivo):

        if nombre_hab in self.habitaciones:

            lista_disps = self.habitaciones[nombre_hab]

            for disp in lista_disps:

                if disp == dispositivo:
                    dispositivo.cambiar_estado(False)
                    print("Dispositivo apagado.")

    def mostrar_hogar (self):

        print ("\nMostrando habitaciones y dispositivos:\n")

        for hab, dispositivos in self.habitaciones.items():

            print("Habitación", hab, ":")

            for disp in dispositivos:

                disp.consultar_params() # como la funcion se llama igual en todos, viene de lujo.