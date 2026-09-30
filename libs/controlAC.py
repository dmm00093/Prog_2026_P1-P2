# Libreria: Control Aire Acondicionado (controlAC)
# Funcion: Gestion de AC
# Funcionalidades:
"""
    - Conocer la temperatura ambiente.
    - Poder cambiar la temperatura del aire acondicionado.
    - Poder cambiar la fuerza del aire.
    - Conocer si está apagado o encendido.
    - Debemos poder apagarlo y encenderlo.
    - Pueda activar/desactivar el modo ahorro energético (tecnología inverter).
    - Pueda obtener una descripción del dispositivo (marca, modelo, etc.).
"""

from libs.controlTemp import tambDefinir

"""
def ACdefinir(tamb):

    # Necesitamos tamb de control temp

    if tamb == None:
        print("ERROR : Temperatura ambiente no definida.")
        return -1

    tAC = int(input("¿Temperatura de AC deseada?: "))
    fAC = int(input("¿Fuerza de AC deseada?: "))
    estadoAC = False # por defecto, apagado
    ahorroAC = False # por defecto, apagado
    descAC = ("ERROR: Definir máquina.")

    unidadAC = {
        "tambiente"  : tamb, # Ya definido en input de la funcion.
        "tempAC"     : tAC ,
        "fuerzaAC"   : fAC ,
        "estadoAC"   : estadoAC,
        "ahorroAC"   : ahorroAC,
        "descAC"     : descAC,
    }

    return unidadAC
"""

def ACdefinir(tamb):

    # Necesitamos tamb de control temp

    if tamb == None:
        print("ERROR : Temperatura ambiente no definida.")
        return -1

    tAC = 0
    fAC = 0
    estadoAC = False  # por defecto, apagado
    ahorroAC = False  # por defecto, apagado
    descAC = ("")

    unidadAC = {
        "tAmbiente"  : tamb, # Ya definido en input de la funcion.
        "tempAC"     : tAC ,
        "fuerzaAC"   : fAC ,
        "estadoAC"   : estadoAC,
        "ahorroAC"   : ahorroAC,
        "descAC"     : descAC,
    }

    tAC = ACtemp(unidadAC)
    fAC = ACfuerza(unidadAC)
    descAC = ACdescripcion(unidadAC)

    return unidadAC

def ACtemp(unidadAC):

    tAC = int(input("¿Temperatura de AC deseada?: "))

    if tAC < 10 or tAC > 30:

        print("ERROR : Valor fuera de rango de la máquina. Asignando 21 ºC.")
        unidadAC["tempAC"] = 21
        return unidadAC

    print("Asignando", tAC, "ºC.")
    unidadAC["tempAC"] = tAC

    return unidadAC

def ACfuerza(unidadAC):

    fAC = int(input("¿Fuerza (%) de AC deseada?: "))

    if fAC <= 0 or fAC > 100:

        print("ERROR : Valor fuera de rango de la máquina. Asignando 50%.")
        unidadAC["fuerzaAC"] = 50
        return unidadAC

    print("Asignando", fAC, "%.")
    unidadAC["fuerzaAC"] = fAC

    return unidadAC

def ACestado(unidadAC):

    if (unidadAC["estadoAC"] == True):

        unidadAC["estadoAC"] = False # apaga

        print("Apagando unidad AC.")

        return unidadAC

    elif (unidadAC["estadoAC"] == False):

        unidadAC["estadoAC"] = True  # enciende

        print("Encendiendo unidad AC.")

        return unidadAC

def ACahorro(unidadAC):

    if (unidadAC["ahorroAC"] == True):

        unidadAC["ahorroAC"] = False  # apaga

        print("Apagando modo ahorro.")

        return unidadAC

    elif (unidadAC["ahorroAC"] == False):

        unidadAC["ahorroAC"] = True  # enciende

        print("Encendiendo modo ahorro.")

        return unidadAC

def ACdescripcion(unidadAC):

    print("Describa la máquina AC: ", end = '')
    unidadAC["descAC"] = input()

    return unidadAC




