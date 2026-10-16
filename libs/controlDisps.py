from libs.bombillaLED import Bombilla
from libs.controlAC import AC
from libs.ansi_colores import color

# ToDo: Todas las funciones que tenia el original, mejorar mostrar_hogar()

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

    def mostrar_hogar (self):

        print ("\nMostrando habitaciones y dispositivos:\n")

        for hab, dispositivos in self.habitaciones.items():

            print("Habitación", hab, ":")

            for disp in dispositivos:

                disp.consultar_params() # como la funcion se llama igual en todos, viene de lujo.

'''
def hogarDefinir ():

    print("\n-----DEFINICIÓN DE HOGAR------")
    print("¿Nº de habitaciones del hogar?: ", end ='')
    numHabs = int(input())

    i = 0
    listaHabs = list()

    while i < numHabs:

        if numHabs == 0:

            print("No hay habitaciones.")
            break

        print("Defina la habitación nº", i+1, ": ", end = '') # para no tener en pantalla habitación 0
        listaHabs.append(input())

        i = i + 1

    hogar = {} # Creamos nuestro diccionario
    for hab in listaHabs:

        hogar[hab] = [] # Añadimos todos los elementos de la lista al diccionario

    return hogar

def hogarIdentificar(hogar):

    print("\nTu hogar tiene las siguientes habitaciones:", hogar.keys())

    print("Tu hogar tiene el siguiente número de habitaciones:", len(hogar))

    return 0

def hogarListar (hogar):

    print("\n-----LISTADO DE DISPOSITIVOS-----")
    print(f"¿Quieres ver todos los dispositivos del hogar? Teclea SI para hacerlo, NO para saltar")

    opcion = input()

    if opcion == 'SI' or opcion == 'si':

        for hab in hogar:

            print(hab, ":")
            print(hogar[hab])

    elif opcion == 'NO' or opcion == 'no':

        print("Tienes las siguientes habitaciones:", hogar.keys())

        print("Teclea la habitación a escoger: ", end = '')
        opcion = input()

        print("Mostrando resultado:")
        print(hogar[opcion])

    else:

        print("Error: entrada incorrecta.")
        return 0

    return 0

def hogarAniadir (hogar):

    print("\n-----AÑADIDO DE DISPOSITIVOS-----")
    print("Tienes las siguientes habitaciones:", hogar.keys()) # listado de claves
                                                               # clave -> habitacion
    print("Teclea la habitación a escoger: ", end='')
    opcion1 = input()

    codigoErr = -1 # si escoge la habitacion correcta, seguiremos

    for key in hogar.keys(): # vemos si existe

        if key == opcion1:
            codigoErr = 0
            break

    if codigoErr == -1: # si no, salimos
        print("Error: no existe.")
        return hogar

    print("Escribe el dispositivo a añadir (bombilla, AC):", end = '')
    opcion2 = input()

    if opcion2 == 'bombilla':

        bombilla = bombillaCrea(False, [30, 30, 30], 200,
                         1,"Bombilla LED")

        hogar[opcion1].append(bombilla)

    elif opcion2 == 'AC' or opcion2 == 'ac':

        AC = ACdefinir(tamb=25) # 25ºC defecto
        hogar[opcion1].append(AC)

    else:

        print("Error: opción errónea.")
        return -1

    return hogar

def hogarQuitar(hogar):

    print("\n-----ELIMINACIÓN DE DISPOSITIVOS-----")
    print("Tienes las siguientes habitaciones:", list(hogar.keys()))

    opcion1 = input("Teclea la habitación a escoger: ")

    codigoErr = -1  # si escoge la habitacion correcta, seguiremos

    for key in hogar.keys():

        if key == opcion1: # vemos si existe
            codigoErr = 0
            break

    if codigoErr == -1: # si no, bye
        print("Error: no existe.")
        return hogar

    lista_disp = hogar[opcion1] # obtenemos la lista de caracteristicas de ese dispositivo

    if len(lista_disp) == 0: # ¿está vacía?
        print("No hay dispositivos en esta habitación para borrar.")
        return hogar

    # mostramos todos los dispositivos.
    # tuve que buscar sobre los for y la funcion in range, no sabia como hacerlo bien.
    print("\nDispositivos en:", opcion1)
    for i in range(len(lista_disp)):

        disp = lista_disp[i]

        # tambien tuve que buscar sobre el .get
        # al parecer busca en el diccionario y si no lo encuentra lo salta y no da eror
        desc = disp.get("descripcion", disp.get("descAC"))

        print(i, ":", desc)

    posicion = int(input("\nIntroduce el número del dispositivo que quieres quitar: "))

    # vemos tambien si el usuario ha cogido el adecuado
    if (0 <= posicion < len(lista_disp)):
        hogar[opcion1].pop(posicion)
        print("Dispositivo eliminado.")
    else:
        print("Error: opción errónea.")

    return hogar

def hogarModDisp (hogar):

    print("\n-----MODIFICADO DE DISPOSITIVOS-----")
    print("Tienes las siguientes habitaciones:", list(hogar.keys()))

    opcion1 = input("Teclea la habitación a escoger: ")

    codigoErr = -1  # si escoge la habitacion correcta, seguiremos

    for key in hogar.keys():

        if key == opcion1:  # vemos si existe
            codigoErr = 0
            break

    if codigoErr == -1:  # si no, bye
        print("Error: no existe.")
        return hogar

    lista_disp = hogar[opcion1]

    if len(lista_disp) == 0:  # ¿está vacía?
        print("No hay dispositivos en esta habitación.")
        return hogar

    # mostramos todos los dispositivos.
    print("\nDispositivos en:", opcion1)

    desc = list()
    disp = 0

    for i in range(len(lista_disp)):
        disp = lista_disp[i]

        desc = disp.get("descripcion", disp.get("descAC"))

        print(i, ":", desc)

    posicion = int(input("\nIntroduce el número del dispositivo que quieres modificar: "))

    print("Teclee lo que desea modificar (ESTADO o DESCRIPCION): ", end = '')
    opcion2 = input()

    if opcion2 == 'ESTADO' or opcion2 == 'estado':

        if "descripcion" in lista_disp[posicion]:

            bombillaEstado(lista_disp[posicion])

        elif "descAC" in lista_disp[posicion]:

            ACestado(lista_disp[posicion])

        else:

            print("Error.")

    elif opcion2 == 'DESCRIPCION' or opcion2 == 'descripcion' or opcion2 == 'desc':

        if "descripcion" in lista_disp[posicion]:

            bombillaDesc(lista_disp[posicion])

        elif "descAC" in lista_disp[posicion]:

            ACdescripcion(lista_disp[posicion])

        else:

            print("Error.")

    return hogar

def hogarRealocDisp (hogar):

    print("\n-----REALOCADO DE DISPOSITIVOS-----")
    print("Tienes las siguientes habitaciones:", list(hogar.keys()))

    opcion1 = input("Teclea la habitación a escoger: ")

    codigoErr = -1  # si escoge la habitacion correcta, seguiremos

    for key in hogar.keys():

        if key == opcion1:  # vemos si existe
            codigoErr = 0
            break

    if codigoErr == -1:  # si no, bye
        print("Error: no existe.")
        return hogar

    lista_disp = hogar[opcion1]

    if len(lista_disp) == 0:  # ¿está vacía?
        print("No hay dispositivos en esta habitación.")
        return hogar

    # mostramos todos los dispositivos.
    print("\nDispositivos en:", opcion1)

    for i in range(len(lista_disp)):
        disp = lista_disp[i]

        desc = disp.get("descripcion", disp.get("descAC"))

        print(i, ":", desc)

    posicion = int(input("\nIntroduce el número del dispositivo que quieres desplazar: "))

    print("¿Dónde quieres desplazarlo?")

    print("Tienes las siguientes habitaciones:", list(hogar.keys()))

    opcion2 = input("Teclea la habitación a escoger: ")

    if opcion2 not in hogar:  # vemos si existe el dispositivo
        print("Error: La habitación no existe.")
        return hogar

    dispositivo = hogar[opcion1].pop(posicion)

    hogar[opcion2].append(dispositivo)

    return hogar
'''


