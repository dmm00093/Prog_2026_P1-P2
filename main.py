# Main: código principal
# Autor: dmm00093@red.ujaen.es
# Función: comprobar mediante texto por pantalla el funcionamiento de todas las librerías.

# -------------------------------------------------------------------------
# 0.1 - Imports
# -------------------------------------------------------------------------

from enum import Enum
import pickle

from libs.ansi_colores import Color
from libs.bombilla import Bombilla
from libs.ac import AC
from libs.hogarDisps import Hogar
from libs.programador import Programador
from libs.dispositivo import Dispositivo

# -------------------------------------------------------------------------
# 0.2 - Funciones
# -------------------------------------------------------------------------

def mostrar_disp(disp):
    print("\n****************************************")
    print("Dispositivo creado satisfactoriamente.", Color.NEGRITA.value, Color.AZUL.value)
    print("Valores por defecto inicializados.", Color.RESET.value)
    print("****************************************\n")
    print(disp.consultar_params_texto())
    print("\nPodrá cambiarlos usando las funciones set_xyz.\n")

def comprobar_return(errcod, operacion):
    if errcod == 0:
        print(Color.VERDE.value, "[OK]", Color.RESET.value, operacion, "realizada correctamente")
    else:
        print(Color.ROJO.value, "[ERROR]", Color.RESET.value, operacion, "falló (código -1).")

def guardar_datos_v2(nomFich, datosFich):

    try:
        with open(nomFich, 'wb') as fichero:
            pickle.dump(datosFich, fichero)
            print(Color.VERDE.value, "Guardado exitoso.", Color.RESET.value)

    except Exception:
        print("error en guardado!")

def cargar_datos_v2(nomFich):

    try:
        with open(nomFich, 'rb') as fichero:
            datos = pickle.load(fichero)
            print(Color.VERDE.value, "Cargado exitoso", Color.RESET.value)
        return datos

    except FileNotFoundError:
        print(Color.ROJO.value, "Error en cargado! Archivo NO EXISTE", Color.RESET.value)
    except Exception:
        print(Color.ROJO.value, "Error en cargado!", Color.RESET.value)

# -------------------------------------------------------------------------
# 1. Dispositivos
# -------------------------------------------------------------------------

LED_1 = Bombilla("LED_1", "LED Azul (1.8V, 1.5 mA)")
mostrar_disp(LED_1)

AC_1 = AC("Daykin 1500", "Daykin de 1500 fgs.", 25)
mostrar_disp(AC_1)

# -------------------------------------------------------------------------
# 1.2 - Pruebas clase dispositivo y manejo de errores
# -------------------------------------------------------------------------

print(Color.AMARILLO.value, "\n····· PRUEBAS ERRORES ·····", Color.RESET.value)
Disp1 = Dispositivo(nivelIntensidad=5, maxIntensidad=10, minIntensidad=0)

estadoOK = False # variable de control para el manejo de errores
incrOK = False
decrOK = False

while (not estadoOK): # bucle infinito mientras estadoOK sea falso.

    try:
        if not incrOK:
            print("Intensidad actual:", Color.AZUL.value, Disp1.get_nivelIntensidad(), Color.RESET.value)
            aumentoIntensidad = int(input("Introduzca aumento de intensidad: "))
            Disp1.aumentarIntensidad(aumentoIntensidad)
            print(Color.VERDE.value, "OK!", Color.RESET.value, "Intensidad aumentada adecuadamente.")
            incrOK = True
        if not decrOK:
            decrementoIntensidad = int(input("Introduzca disminución de intensidad: "))
            Disp1.disminuirIntensidad(decrementoIntensidad)
            print(Color.VERDE.value, "OK!", Color.RESET.value, "Intensidad disminuida adecuadamente.")
            decrOK = True

        estadoOK = True
        print(Color.VERDE.value, "OK!", Color.RESET.value, "Intensidades modificadas adecuadamente.")

    except ValueError:
        print(Color.ROJO.value, "Error en el valor introducido (inválido o no existente),",
              Color.RESET.value, "inténtelo de nuevo.")
    except Exception:
        print(Color.ROJO.value, "Error en el dato introducido (inválido o no existente)",
              Color.RESET.value, ", inténtelo de nuevo.")

print("FIN PRUEBAS INTENSIDAD.")

# -------------------------------------------------------------------------
# 4. Pruebas Hogar
# -------------------------------------------------------------------------

mi_hogar = Hogar() # definicion de hogar

# creacion y añadido de habitaciones sin prints para ver fichero cargado facil
mi_hogar.crear_habitacion("Salón")
mi_hogar.crear_habitacion("Dormitorio")

mi_hogar.add_dispositivo("Salón", AC_1)
mi_hogar.add_dispositivo("Salón", LED_1)

# -------------------------------------------------------------------------
# 5. Ficheros
# -------------------------------------------------------------------------

print(Color.AZUL.value, "\n····· PRUEBAS FICHEROS ·····", Color.RESET.value)

# --- test errores ficheros --- #

hogarNuevoErr = cargar_datos_v2('HogarData') # efectivamente devuelve error si HogarData no existe
hogarNuevoErr2 = cargar_datos_v2('ArchivoFalso') # otro error que si o sí saldrá

fichero = 'HogarData'  # nombre del fichero a cargar y guardar.
guardar_datos_v2(fichero, mi_hogar)
hogarNuevo = cargar_datos_v2(fichero)

if hogarNuevo is not None:
    print("\nMostrando fichero cargado:")
    print(hogarNuevo.mostrar_hogar_texto())


