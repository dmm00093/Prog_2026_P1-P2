# Necesitamos un metodo (funcion), que nos devolverá la estructura de la bombilla LED.
# Ir probando el código para que funcione cada cosa necesaria.

def bombillaCrea(estado, color, intensidad, nivelblanco, descripcion):

    # Funcion : Creamos un diccionario para la bombilla.

    # param estado : TRUE -> ON - FALSE -> OFF
    # param color : lista con los valores RGB.
    # param intensidad : intensidad luminosa valor de 1 a 255 (0 no, estaria apagado)
    # param nivelBlanco : 1 frio, 2 suave, 3 calido
    # param descripcion : string con marca y modelos

    return {"estado"      : estado,
            "color"       : color,
            "intensidad"  : intensidad,
            "nivelBlanco" : nivelblanco,
            "descripcion" : descripcion,
            }

""" def bombillaCrea2():

    # Funcion : Creamos un diccionario para la bombilla introducido por el usuario.

    color = list()
    intensidad = 0
    nivelblanco = 0
    description = list ()

    i = 0

    while i < 5:

        if i == 0:
            estado = bool(input("¿Está encendida?"))

        if i == 1:

            colorNuevo = list()

            colorNuevo.append(int(input("Escoja el valor de ROJO  (R):")))
            colorNuevo.append(int(input("Escoja el valor de VERDE (G):")))
            colorNuevo.append(int(input("Escoja el valor de AZUL  (B):")))

            j = 0
            listaColoresError = ["R", "G", "B"]

            while (j < len(listaColoresError)):

                if colorNuevo[i] > 255:
                    print("ERROR: El valor del color", listaColoresError[i],
                          "es erróneo. Estableciendo valor predeterminado [255].")
                    colorNuevo[i] = 255

                j += 1

        if i == 2:

            intensidad = int(input("Intensidad deseada (de 0 hasta 255):"))

            if intensidad == 0:
                print("Apagando...")
                intensidad = False

            if intensidad > 255:
                print("Error. Asignando 255.")
                intensidad = 255

        if i == 3:

            print("\nIntroduzca el tono de blanco deseado:\n{ 1 -> FRIO } , { 2 -> SUAVE } , { 3 -> CALIDO }\n")

            nivelB = int(input("Introduzca su opción: "))  # tono de blanco

            if 1 > nivelB or nivelB > 3:

                print("Inválido. Estableciendo valor frío por defecto.")

                bombilla["nivelblanco"] = nivelB
                return bombilla

            else:

                print("Estableciendo nivel", nivelB, "de blanco")

                bombilla["nivelblanco"] = nivelB
                return bombilla

        i += 1

    # param estado : TRUE -> ON - FALSE -> OFF
    # param color : lista con los valores RGB.
    # param intensidad : intensidad luminosa valor de 1 a 255 (0 no, estaria apagado)
    # param nivelBlanco : 1 frio, 2 suave, 3 calido
    # param descripcion : string con marca y modelos

    return {"estado"      : estado,
            "color"       : color,
            "intensidad"  : intensidad,
            "nivelBlanco" : nivelblanco,
            "descripcion" : descripcion,
            }
"""

def bombillaEstado (bombilla):

    # Funcion : Enciende una bombilla.

    if (bombilla["estado"] == False):

        bombilla["estado"] = True
        print("Encendiendo bombilla.")

    else:

        bombilla["estado"] = False
        print("Apagando bombilla.")

    return bombilla

def bombillaIntensidad (bombilla):

    # Funcion: Cambiar intensidad de bombilla.

    bombilla["intensidad"] = int(input("Intensidad deseada (de 0 hasta 255):"))

    if bombilla["intensidad"] == 0:

        print("Apagando...")
        bombilla["estado"] = False

    if bombilla["intensidad"] > 255:

        print("Error. Asignando 255.")
        bombilla["intensidad"] = 255
        return bombilla

    print("Intensidad modificada.")

    return bombilla

def bombillaColor (bombilla):

    # Funcion: Cambiar color de bombilla con lista RGB

    colorNuevo = list()

    colorNuevo.append(int(input("Escoja el valor de ROJO  (R):")))
    colorNuevo.append(int(input("Escoja el valor de VERDE (G):")))
    colorNuevo.append(int(input("Escoja el valor de AZUL  (B):")))

    i = 0
    listaColoresError = ["R", "G", "B"]

    while (i < len(listaColoresError)):

        if colorNuevo[i] > 255:

            print("ERROR: El valor del color", listaColoresError[i], "es erróneo. Estableciendo valor predeterminado [255].")
            colorNuevo[i] = 255

        i += 1

    bombilla["color"] = colorNuevo
    print("Asignando color RGB:",colorNuevo)

    return bombilla

def bombillaNivelB (bombilla):

    print("Introduzca el tono de blanco deseado:\n{ 1 -> FRIO } , { 2 -> SUAVE } , { 3 -> CALIDO }\n")

    nivelB = int(input("Introduzca su opción: ")) # tono de blanco

    if 1>nivelB or nivelB>3:

        print("Inválido. Estableciendo valor frío por defecto.")

        bombilla["nivelBlanco"] = 1
        return bombilla

    else:

        print("Estableciendo nivel", nivelB, "de blanco")

        bombilla["nivelBlanco"] = nivelB
        return bombilla

def bombillaDesc (bombilla):

    print("Defina la bombilla: ", end = '')

    bombilla["descripcion"] = input()

    return bombilla