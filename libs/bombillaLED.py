from libs.ansi_colores import color

class Bombilla:

    def __init__(self, nombre, descripcion):

        self.estado = False
        self.color = [255, 255, 255]
        self.intensidad = 200
        self.nivelblanco = 2
        self.descripcion = descripcion
        self.nombre = nombre

        print("\n****************************************")
        print("Dispositivo creado satisfactoriamente.", color.NEGRITA, color.AZUL)
        print("Valores por defecto inicializados.", color.RESET)
        print("****************************************\n")
        self.consultar_params()
        print("\nPodrá cambiarlos usando las funciones cambiar_xyz.\n")

    def cambiar_estado(self, estado):

        self.estado = estado

    def cambiar_intensidad(self, intensidad):

        if intensidad == 0:

            print("Apagando bombilla.")
            self.estado = False

        elif intensidad > 255:

            print("Error de valor. Asignando 255 por defecto.")
            self.intensidad = 255

        else:

            print("Asignando una intensidad de", intensidad)
            self.intensidad = intensidad

    def cambiar_color(self, R, G, B):

        colorNuevo = [R, G, B]

        i = 0
        listaColoresError = ["R", "G", "B"]

        while (i < len(listaColoresError)):

            if colorNuevo[i] > 255:
                print("ERROR: El valor del color", listaColoresError[i],
                      "es erróneo. Estableciendo valor predeterminado [255].")
                colorNuevo[i] = 255

            i += 1

        self.color = colorNuevo
        print("Asignando color RGB:", colorNuevo)

    def cambiar_nivel_blanco(self, nivelblanco):

        if 1 > nivelblanco or nivelblanco > 3:

            print("Inválido. Estableciendo valor frío por defecto.")

            self.nivelblanco = 1

        else:

            print("Estableciendo nivel", nivelblanco, "de blanco")

            self.nivelblanco = nivelblanco

    def cambiar_descripcion(self, descripcion):

        self.descripcion = descripcion

    def consultar_params(self):

        # mismo nombre en todos los dispositivos para facilitar mostrar informacion en hogar

        if self.estado == True:
            display = "ON"
        else:
            display = "OFF"

        print("Parámetros de", self.nombre, ":")
        print(f"Estado:", display, "\nColor:", self.color, "\nIntensidad:", self.intensidad,
              "\nNivel de Blanco:", self.nivelblanco, "\nDescripcion:", self.descripcion)
