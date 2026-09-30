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

def ACdefinir(tamb):

    # Necesitamos tamb de control temp primero. Definido externamente. El aire no decide la temperatura ambiente.
    # Seria un sensor pero no tenemos eso aun

    if tamb == None: # Si no existe, salimos. O estamos todos muertos o es que no se ha definido tamb.
        print("ERROR : Temperatura ambiente no definida.")
        return -1

    tAC = 0
    fAC = 0
    estadoAC = False  # por defecto, apagado
    ahorroAC = False  # por defecto, apagado
    descAC = ("")

    # diccionario de la unidad
    unidadAC = {
        "tAmbiente"  : tamb, # Ya definido en input de la funcion.
        "tempAC"     : tAC ,
        "fuerzaAC"   : fAC ,
        "estadoAC"   : estadoAC,
        "ahorroAC"   : ahorroAC,
        "descAC"     : descAC,
    }

    # Como estas funciones modifican la clave, directamente, solo las llamamos y tirando. Antes hice algo así:
    # tAC = ACtemp(unidadAC)
    # Pero esto es redundante. Porque ACtemp, lo que modifica, es unidadAC["tAC"], no le asigna un valor externo.

    ACtemp(unidadAC)
    ACfuerza(unidadAC)
    ACdescripcion(unidadAC)

    return unidadAC

def ACtemp(unidadAC):

    tAC = int(input("¿Temperatura de AC deseada?: "))

    if tAC < 10 or tAC > 30: # la maquina no llega a estos valores.

        print("ERROR : Valor fuera de rango de la máquina. Asignando 21 ºC.")
        unidadAC["tempAC"] = 21
        return unidadAC

    print("Asignando", tAC, "ºC.")
    unidadAC["tempAC"] = tAC

    return unidadAC

def ACfuerza(unidadAC):

    fAC = int(input("¿Fuerza (%) de AC deseada?: "))

    if fAC <= 0 or fAC > 100: # la maquina solo puede funcionar de 1 a 100 %.

        print("ERROR : Valor fuera de rango de la máquina. Asignando 50%.")
        unidadAC["fuerzaAC"] = 50
        return unidadAC

    print("Asignando", fAC, "%.")
    unidadAC["fuerzaAC"] = fAC

    return unidadAC

def ACestado(unidadAC):

    if (unidadAC["estadoAC"] == True): # Simulo una conmutación por un botón externo, puede ser un mando.

        unidadAC["estadoAC"] = False # apaga

        print("Apagando unidad AC.")

        return unidadAC

    elif (unidadAC["estadoAC"] == False):

        unidadAC["estadoAC"] = True  # enciende

        print("Encendiendo unidad AC.")

        return unidadAC

def ACahorro(unidadAC):

    if (unidadAC["ahorroAC"] == True): # Igual, conmutación por un botón del mando.

        unidadAC["ahorroAC"] = False  # apaga

        print("Apagando modo ahorro.")

        return unidadAC

    elif (unidadAC["ahorroAC"] == False):

        unidadAC["ahorroAC"] = True  # enciende

        print("Encendiendo modo ahorro.")

        return unidadAC

def ACdescripcion(unidadAC):

    print("Describa la máquina AC: ", end = '') # descripcion sencilla.
    unidadAC["descAC"] = input()

    return unidadAC




