from libs.bombillaLED import (bombillaCrea, bombillaEncender,
                              bombillaColor, bombillaDesc,
                              bombillaIntensidad, bombillaNivelB)

from libs.controlAC import (ACdescripcion, ACfuerza, ACahorro,
                            ACdefinir, ACestado, ACtemp)

from libs.controlTemp import tambDefinir

from libs.controlDisps import (hogarDefinir, hogarIdentificar,
                               hogarAniadir, hogarQuitar, hogarListar, hogarModDisp, hogarRealocDisp)

# -------- Funciones Bombilla ----------

LED = bombillaCrea(False, [255, 255, 255], 50, 3, "Bombilla LED")

bombillaEncender(LED)
bombillaColor(LED)
bombillaDesc(LED)
bombillaIntensidad(LED)
bombillaNivelB(LED)

# -------- Funciones Aire ----------

tamb = tambDefinir()

aire = ACdefinir(tamb)
ACdescripcion(aire)
ACfuerza(aire)
ACahorro(aire)
ACestado(aire)
ACtemp(aire)

# -------- Funciones Hogar ----------

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
