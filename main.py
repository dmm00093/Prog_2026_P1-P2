from libs.bombillaLED import (bombillaCrea, bombillaEncender,
                              bombillaColor, bombillaDesc,
                              bombillaIntensidad, bombillaNivelB)

from libs.controlAC import (ACdescripcion, ACfuerza, ACahorro,
                            ACdefinir, ACestado, ACtemp)

from libs.controlTemp import tambDefinir

# Definición de Parámetros a manipular
# ------------------------------------

ledCuarto = bombillaCrea(False, [30, 30, 30], 200,
                         1,"Bombilla LED del cuarto")

tamb = tambDefinir()

unidadAC = ACdefinir(tamb)

print("Bombilla:")
print(ledCuarto)
print("Aire:")
print(unidadAC)

# Uso de funcionalidades para manipularlos
# ----------------------------------------

ACtemp(unidadAC)
ACestado(unidadAC)
ACahorro(unidadAC)
ACfuerza(unidadAC)
ACdescripcion(unidadAC)

print(unidadAC)