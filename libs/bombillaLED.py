# Necesitamos un metodo (funcion), que nos devolverá la estructura de la bombilla LED.
# Ir probando el código para que funcione cada cosa necesaria.

def creaBombilla(estado, color, intensidad, nivelblanco, descripcion):

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

def encenderBombilla(bombilla):

    # Funcion : Enciende una bombilla.

    bombilla["estado"] = True

    return bombilla