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

    fichero = open(nomFich, 'wb')
    pickle.dump(datosFich, fichero)
    fichero.close()
    return 0

def cargar_datos_v2(nomFich):

    fichero = open(nomFich, 'rb')
    datos = pickle.load(fichero)
    fichero.close()

    return datos

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

estadoOK = False # variable de control para el manejo de errores

while (not estadoOK): # bucle infinito mientras estadoOK sea falso.
    try:
        D1 = Dispositivo("Dispositivo 1")
        print("Dispositivo 1 creado")
        estadoOK = True

        D1.cambiarNombre(25)

    except TypeError:
        print("Error en la cadena de caracteres (inválida o no existente)")
    except ValueError:
        print("Error en el valor (inválido o no existente)")
    except Exception:
        print("Error en el input (inválido o no existente)")

print("FIN.")

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

print(Color.NEGRITA.value, "\nPRUEBAS FICHEROS", Color.RESET.value)

fichero = 'HogarData' # nombre del fichero a cargar y guardar.

checkErr = guardar_datos_v2(fichero, mi_hogar)
if checkErr == 0: # TODO (1): Manejo de errores. Esto no sirve.
    print(Color.AZUL.value, "Guardado OK", Color.RESET.value)
else:
    print(Color.ROJO.value, "Guardado ERROR", Color.RESET.value)

hogarNuevo = cargar_datos_v2(fichero)
if hogarNuevo != '': # TODO (2): Manejo de errores. Esto no sirve.
    print(Color.AZUL.value, "Cargado OK", Color.RESET.value)
else:
    print(Color.ROJO.value, "Cargado ERROR", Color.RESET.value)

print("\nMostrando fichero cargado:")
print(hogarNuevo.mostrar_hogar_texto())