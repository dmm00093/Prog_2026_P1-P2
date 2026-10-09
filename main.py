from libs.bombillaLED import (bombillaCrea, bombillaEstado,
                              bombillaColor, bombillaDesc,
                              bombillaIntensidad, bombillaNivelB)

from libs.controlAC import (ACdescripcion, ACfuerza, ACahorro,
                            ACdefinir, ACestado, ACtemp)

from libs.controlTemp import tambDefinir

from libs.controlDisps import (hogarDefinir, hogarIdentificar,
                               hogarAniadir, hogarQuitar, hogarListar, hogarModDisp, hogarRealocDisp)

# -------- Funciones Bombilla ----------

LED = bombillaCrea(False, [255, 255, 255], 50, 3, "Bombilla LED")

print("\nFUNCIONES BOMBILLA:")
print("-----------------")
print("Bombilla actual:", LED)
bombillaEstado(LED)
bombillaColor(LED)
bombillaDesc(LED)
bombillaIntensidad(LED)
bombillaNivelB(LED)
print("Bombilla tras los cambios:")
print(LED)

# -------- Funciones Aire ----------

tamb = tambDefinir()

print("\nFUNCIONES AC:")
print("-----------------")
aire = ACdefinir(tamb)
ACdescripcion(aire)
ACfuerza(aire)
ACahorro(aire)
ACestado(aire)
ACtemp(aire)
print("AC tras los cambios:")
print(aire)

# -------- Funciones Hogar ----------

print("\nFUNCIONES HOGAR:")
print("-----------------")
hogar = hogarDefinir()
hogarIdentificar(hogar)

hogarAniadir(hogar)
hogarListar(hogar)

hogarModDisp(hogar)
hogarListar(hogar)

hogarRealocDisp(hogar)
hogarListar(hogar)

hogarQuitar(hogar)
hogarListar(hogar)
