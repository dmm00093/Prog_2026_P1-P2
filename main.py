import sys

from libs.bombillaLED import creaBombilla, encenderBombilla

ledCuarto = creaBombilla(False, [30, 30, 30], 200,
                         1,"Bombilla LED del cuarto xd")

print(ledCuarto)

encenderBombilla (ledCuarto)

print(ledCuarto)