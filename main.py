from libs.bombillaLED import Bombilla
from libs.controlAC import AC
from libs.controlDisps import Hogar

# Instancias de los dispositivos
LED_1 = Bombilla("LED_1", "LED Azul (1.8V, 1.5 mA)")
AC_1  = AC("Daykin 1500", "Daykin de 1500 fgs.", 25)

casa1 = Hogar()

print("1. Probando crear_habitacion")
casa1.crear_habitacion('Salón')
casa1.crear_habitacion('Dormitorio')
casa1.crear_habitacion('Salón')  # Debe avisar que ya existe

print("\n2. Probando add_dispositivo")
casa1.add_dispositivo('Salón', LED_1)
casa1.add_dispositivo('Salón', AC_1)
casa1.add_dispositivo('Cocina', LED_1)  # Debe dar error de habitación inexistente

casa1.mostrar_hogar()

print("3. Probando encender_dispositivo")
casa1.encender_dispositivo('Salón', LED_1)
casa1.encender_dispositivo('Salón', AC_1)

casa1.mostrar_hogar()

print("4. Probando apagar_dispositivo")
casa1.apagar_dispositivo('Salón', LED_1)

casa1.mostrar_hogar()

print("5. Probando mover_dispositivo")
casa1.mover_dispositivo('Salón', 'Dormitorio', AC_1)

casa1.mostrar_hogar()

print("6. Probando quitar_dispositivo")
casa1.quitar_dispositivo('Salón', LED_1)

print("\nEstado final")
casa1.mostrar_hogar()
