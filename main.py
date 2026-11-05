# Main: código principal
# Autor: dmm00093@red.ujaen.es
# Función: comprobar mediante texto por pantalla el funcionamiento de todas las librerías.

from enum import Enum

from libs.ansi_colores import Color
from libs.bombilla import Bombilla
from libs.ac import AC
from libs.hogarDisps import Hogar
from libs.programador import Programador
from libs.dispositivo import Dispositivo

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

# -------------------------------------------------------------------------
# 1. Dispositivos
# -------------------------------------------------------------------------
LED_1 = Bombilla("LED_1", "LED Azul (1.8V, 1.5 mA)")
mostrar_disp(LED_1)

AC_1 = AC("Daykin 1500", "Daykin de 1500 fgs.", 25)
mostrar_disp(AC_1)

# -------------------------------------------------------------------------
# Pruebas clase dispositivo y manejo de errores #
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

'''
# -------------------------------------------------------------------------
# 2. Pruebas AC
# -------------------------------------------------------------------------
print(Color.NEGRITA.value, "\nPRUEBAS CLASE AC", Color.RESET.value)

# llamadas válidas
comprobar_return(AC_1.set_nombre("Daikin Salon"), "Cambiar nombre AC")
comprobar_return(AC_1.set_descripcion("Daikin Inverter 3000"), "Cambiar descripción AC")
comprobar_return(AC_1.set_tamb(28), "Cambiar temperatura ambiente")
comprobar_return(AC_1.set_temp(24), "Cambiar temperatura (24ºC)")
comprobar_return(AC_1.set_fuerza(80), "Cambiar fuerza (80%)")
comprobar_return(AC_1.set_estado(True), "Encender AC")
comprobar_return(AC_1.set_ahorro(True), "Activar modo ahorro AC")

# llamadas erróneas
comprobar_return(AC_1.set_temp(35), "Cambiar a temperatura inválida (35ºC)")
comprobar_return(AC_1.set_fuerza(150), "Cambiar a fuerza inválida (150%)")

# gets
print("\nMétodos get de AC:")
print("- ID AC:", AC_1.get_idAC()) # nuevo get en las clases, por lo del contador
print("- Nombre:", AC_1.get_nombre())
print("- Descripción:", AC_1.get_descripcion())
print("- Temp Ambiente:", AC_1.get_tamb(), "ºC")
print("- Temp Programada:", AC_1.get_temp(), "ºC")
print("- Fuerza:", AC_1.get_fuerza(), "%")
print("- Estado:", AC_1.get_estado())
print("- Modo Ahorro:", AC_1.get_ahorro())

# -------------------------------------------------------------------------
# 3. Pruebas bombilla
# -------------------------------------------------------------------------
print(Color.NEGRITA.value, "\nPRUEBAS CLASE BOMBILLA", Color.RESET.value)

# llamadas válidas
comprobar_return(LED_1.set_nombre("Bombilla Techo"), "Cambiar nombre bombilla")
comprobar_return(LED_1.set_descripcion("LED RGB 10W"), "Cambiar descripción bombilla")
comprobar_return(LED_1.set_estado(True), "Encender bombilla")
comprobar_return(LED_1.set_intensidad(150), "Cambiar intensidad (150)")
comprobar_return(LED_1.set_color(250, 100, 50), "Cambiar color (250, 100, 50)")
comprobar_return(LED_1.set_nivelblanco(3), "Cambiar nivel blanco (3)")

# llamadas erróneas
comprobar_return(LED_1.set_intensidad(300), "Cambiar a intensidad inválida (300)")
comprobar_return(LED_1.set_color(300, 100, 50), "Cambiar a RGB inválido (300, 100, 50)")
comprobar_return(LED_1.set_nivelblanco(5), "Cambiar a nivel de blanco inválido (5)")

# gets
print("\nMétodos get de Bombilla:")
print("- ID Bombilla:", LED_1.get_idBombilla()) # nuevo get en las clases, por lo del contador
print("- Nombre:", LED_1.get_nombre())
print("- Descripción:", LED_1.get_descripcion())
print("- Estado:", LED_1.get_estado())
print("- Intensidad:", LED_1.get_intensidad())
print("- Color:", LED_1.get_color())
print("- Nivel Blanco:", LED_1.get_nivelblanco())

# -------------------------------------------------------------------------
# 4. Pruebas Hogar
# -------------------------------------------------------------------------
print(Color.NEGRITA.value, "\nPRUEBAS CLASE HOGAR", Color.RESET.value)

mi_hogar = Hogar()

# crear habitaciones
comprobar_return(mi_hogar.crear_habitacion("Salón"), "Crear habitación Salón")
comprobar_return(mi_hogar.crear_habitacion("Dormitorio"), "Crear habitación Dormitorio")
comprobar_return(mi_hogar.crear_habitacion("Salón"), "Crear habitación duplicada (Salón)")

# añadir dispositivos
comprobar_return(mi_hogar.add_dispositivo("Salón", AC_1), "Añadir AC a Salón")
comprobar_return(mi_hogar.add_dispositivo("Salón", LED_1), "Añadir bombilla a Salón")
comprobar_return(mi_hogar.add_dispositivo("Cocina", LED_1), "Añadir dispositivo a habitación inexistente")

# mover dispositivos
comprobar_return(mi_hogar.mover_dispositivo("Salón", "Dormitorio", LED_1), "Mover bombilla de Salón a Dormitorio")
comprobar_return(mi_hogar.mover_dispositivo("Cocina", "Dormitorio", LED_1), "Mover desde habitación inexistente")

# mostrar estado
print(mi_hogar.mostrar_hogar_texto())

# quitar dispositivo
comprobar_return(mi_hogar.quitar_dispositivo("Dormitorio", LED_1), "Quitar bombilla de Dormitorio")
comprobar_return(mi_hogar.quitar_dispositivo("Cocina", LED_1), "Quitar dispositivo de habitación inexistente")

# mostrar estado final
print(mi_hogar.mostrar_hogar_texto())

# -------------------------------------------------------------------------
# 5. Pruebas Programador (nuevo, p3)
# -------------------------------------------------------------------------
print(Color.NEGRITA.value, "\nPRUEBAS CLASE PROGRAMADOR", Color.RESET.value)

# métodos de clase
print("Métodos de clase Programador:")
print("- Días de la semana válidos:", Programador.getDiasSemana())
print("- Hora actual del sistema:", Programador.getHoraSistema())

# creación de instancia vinculada a bombilla
prog1 = Programador(LED_1)

# añadir eventos de programación
prog1.comienzo("Lunes", 9, 0, 0)
prog1.fin("Lunes", 13, 30, 0)
prog1.comienzo("Viernes", 20, 15, 0)

# getProgramacion
print("\nProgramación de la bombilla (getProgramacion):")
print(prog1.getProgramacion())

# borrar evento
prog1.borrar("Lunes", 9, 0, 0)

print("\nProgramación tras borrar evento (Lunes 09:00:00):")
print(prog1.getProgramacion())
'''