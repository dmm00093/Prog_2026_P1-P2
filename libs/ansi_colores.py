# Libreria: (Clase: color) Valores ANSI para formato de texto.
# Autor: dmm00093@red.ujaen.es (solamente la creación de la clase, valores ANSI --> Google).
# Funcion: posibilidad de añadir formatos de texto con grosor y colores.

class color:

    # Reset -> Resetea color y formato. Negrita -> Negrita.
    RESET = "\033[0m"
    NEGRITA = "\033[1m"

    # Colores
    ROJO = "\033[31m"
    VERDE = "\033[32m"
    AMARILLO = "\033[33m"
    AZUL = "\033[34m"
    CYAN = "\033[36m"