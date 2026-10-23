from libs.ansi_colores import color
from libs.bombillaLED import Bombilla
from libs.controlAC import AC
from libs.controlDisps import Hogar

def mostrar_disp(disp):
    print("\n****************************************")
    print("Dispositivo creado satisfactoriamente.", color.NEGRITA, color.AZUL)
    print("Valores por defecto inicializados.", color.RESET)
    print("****************************************\n")
    print(disp.consultar_params_texto())
    print("\nPodrá cambiarlos usando las funciones set_xyz.\n")

def comprobar_return(errcod, operacion):
    if errcod == 0:
        print(color.VERDE, "[OK]", color.RESET, operacion, "realizada correctamente")
    else:
        print(color.ROJO, "[ERROR]", color.RESET, operacion, "falló (código -1).")

# -------------------------------------------------------------------------
# 1. Dispositivos
# -------------------------------------------------------------------------
LED_1 = Bombilla("LED_1", "LED Azul (1.8V, 1.5 mA)")
mostrar_disp(LED_1)

AC_1 = AC("Daykin 1500", "Daykin de 1500 fgs.", 25)
mostrar_disp(AC_1)

# -------------------------------------------------------------------------
# 2. Pruebas AC
# -------------------------------------------------------------------------
print(color.NEGRITA, "\nPRUEBAS CLASE AC", color.RESET)

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
comprobar_return(AC_1.set_fuerza(150), "Cambiar a fuerza errónea (150%)")

# gets
print("\nMétodos get de AC:")
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
print(color.NEGRITA, "\nPRUEBAS CLASE BOMBILLA", color.RESET)

# llamadas válidas
comprobar_return(LED_1.set_nombre("Bombilla Techo"), "Cambiar nombre Bombilla")
comprobar_return(LED_1.set_descripcion("LED RGB 10W"), "Cambiar descripción Bombilla")
comprobar_return(LED_1.set_estado(True), "Encender Bombilla")
comprobar_return(LED_1.set_intensidad(150), "Cambiar intensidad (150)")
comprobar_return(LED_1.set_color(250, 100, 50), "Cambiar color RGB (250, 100, 50)")
comprobar_return(LED_1.set_nivelblanco(3), "Cambiar nivel blanco (3)")

# llamadas erróneas
comprobar_return(LED_1.set_intensidad(300), "Cambiar intensidad inválida (300)")
comprobar_return(LED_1.set_color(300, 100, 50), "Cambiar color RGB inválido (300, 100, 50)")
comprobar_return(LED_1.set_nivelblanco(5), "Cambiar nivel blanco inválido (5)")

# gets
print("\nMétodos get de Bombilla:")
print("- Nombre:", LED_1.get_nombre())
print("- Descripción:", LED_1.get_descripcion())
print("- Estado:", LED_1.get_estado())
print("- Intensidad:", LED_1.get_intensidad())
print("- Color:", LED_1.get_color())
print("- Nivel Blanco:", LED_1.get_nivelblanco())

# -------------------------------------------------------------------------
# 4. Pruebas Hogar
# -------------------------------------------------------------------------
print(color.NEGRITA, "\nPRUEBAS CLASE HOGAR", color.RESET)

mi_hogar = Hogar()

# crear habitaciones
comprobar_return(mi_hogar.crear_habitacion("Salón"), "Crear habitación Salón")
comprobar_return(mi_hogar.crear_habitacion("Dormitorio"), "Crear habitación Dormitorio")
comprobar_return(mi_hogar.crear_habitacion("Salón"), "Crear habitación duplicada (Salón)")

# añadir dispositivos
comprobar_return(mi_hogar.add_dispositivo("Salón", AC_1), "Añadir AC a Salón")
comprobar_return(mi_hogar.add_dispositivo("Salón", LED_1), "Añadir Bombilla a Salón")
comprobar_return(mi_hogar.add_dispositivo("Cocina", LED_1), "Añadir dispositivo a habitación inexistente")

# mover dispositivos
comprobar_return(mi_hogar.mover_dispositivo("Salón", "Dormitorio", LED_1), "Mover Bombilla de Salón a Dormitorio")
comprobar_return(mi_hogar.mover_dispositivo("Cocina", "Dormitorio", LED_1), "Mover desde habitación inexistente")

# mostrar estado
print(mi_hogar.mostrar_hogar_texto())

# quitar dispositivo
comprobar_return(mi_hogar.quitar_dispositivo("Dormitorio", LED_1), "Quitar Bombilla de Dormitorio")
comprobar_return(mi_hogar.quitar_dispositivo("Cocina", LED_1), "Quitar dispositivo de habitación inexistente")

# mostrar estado final
print(mi_hogar.mostrar_hogar_texto())