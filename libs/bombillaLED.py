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

def bombillaEncender (bombilla):

    # Funcion : Enciende una bombilla.

    bombilla["estado"] = True

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

    return bombilla

def bombillaNivelB (bombilla):

    print("\nIntroduzca el tono de blanco deseado:\n{ 1 -> FRIO } , { 2 -> SUAVE } , { 3 -> CALIDO }\n")

    nivelB = int(input("Introduzca su opción: ")) # tono de blanco

    if 1>nivelB or nivelB>3:

        print("Inválido. Estableciendo valor frío por defecto.")

        bombilla["nivelblanco"] = nivelB
        return bombilla

    else:

        print("Estableciendo nivel", nivelB, "de blanco")

        bombilla["nivelblanco"] = nivelB
        return bombilla

def bombillaDesc (bombilla):

    print("Defina la bombilla: ", end = '')

    bombilla["descripcion"] = input()

    return bombilla