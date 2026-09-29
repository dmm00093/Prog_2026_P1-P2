import sys

from libs.bombillaLED import (bombillaCrea, bombillaEncender,
                              bombillaColor, bombillaDesc,
                              bombillaIntensidad, bombillaNivelB)

print("Bombilla:")

ledCuarto = bombillaCrea(False, [30, 30, 30], 200,
                         1,"Bombilla LED del cuarto")

print(ledCuarto)

bombillaNivelB(ledCuarto)
bombillaIntensidad(ledCuarto)
bombillaDesc(ledCuarto)
bombillaColor(ledCuarto)
bombillaEncender(ledCuarto)

print(ledCuarto)