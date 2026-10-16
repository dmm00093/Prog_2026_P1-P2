# Libreria: Control Aire Acondicionado (controlAC)
# Funcion: Gestion de AC
# Funcionalidades:
"""
    - Conocer la temperatura ambiente.
    - Poder cambiar la temperatura del aire acondicionado.
    - Poder cambiar la fuerza del aire.
    - Conocer si está apagado o encendido.
    - Debemos poder apagarlo y encenderlo.
    - Pueda activar/desactivar el modo ahorro energético (tecnología inverter).
    - Pueda obtener una descripción del dispositivo (marca, modelo, etc.).
"""

from libs.ansi_colores import color

class AC:

    def __init__(self, nombre, descripcion, tamb=25):  # asume 25ºC si no se especifica

        self.tamb = tamb
        self.temp = 22
        self.fuerza = 50
        self.estado = False
        self.ahorro = False
        self.descripcion = descripcion
        self.nombre = nombre

        print("\nDispositivo creado satisfactoriamente.\n", color.NEGRITA, color.AZUL)
        print("Valores por defecto inicializados.\n", color.RESET)
        self.consultar_params_ac()
        print("\nPodrá cambiarlos usando las funciones cambiar_xyz.")

    def cambiar_temp(self, temp):

        if temp < 10 or temp > 30:

            print("ERROR: Fuera de rango. Asignando 21ºC.")
            self.temp = 21

        else:

            print("Asignando", temp, "ºC")
            self.temp = temp

    def cambiar_fuerza(self, fuerza):

        if fuerza <= 0 or fuerza > 100:

            print("ERROR : Valor fuera de rango de la máquina. Asignando 50%.")
            self.fuerza = 50

        else:

            print("Asignando", fuerza, "%.")
            self.fuerza = fuerza

    def cambiar_estado(self, estado):

        self.estado = estado

    def cambiar_modo_ahorro(self, ahorro):

        self.ahorro = ahorro

    def cambiar_descripcion(self, descripcion):

        self.descripcion = descripcion

    def consultar_params_ac(self):

        if self.estado == True:
            display = "ON"
        else:
            display = "OFF"

        print("Parámetros de", self.nombre, ":")

        print("\nTemperatura ambiente (ºC):", self.tamb, "\nTemperatura programada (ºC):", self.temp, "\nFuerza (%):", self.fuerza,
              "\nEstado:", display,
              "\n¿Modo ahorro activo?:", self.ahorro, "\nDescripcion:", self.descripcion)

