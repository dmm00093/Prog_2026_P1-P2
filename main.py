from libs.bombillaLED import Bombilla

from libs.controlAC import AC

from libs.controlDisps import Hogar

from libs.ansi_colores import color

LED_1 = Bombilla("LED_1", "LED Azul (1.8V, 1.5 mA)")
AC_1  = AC("Daykin 1500", "Daykin de 1500 fgs.", 25)

casa1 = Hogar()
casa1.crear_habitacion('Salón')
casa1.add_dispositivo('Salón', LED_1)
casa1.mostrar_hogar()
