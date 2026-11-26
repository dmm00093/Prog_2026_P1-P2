import pickle

class fichManager:

    # guardado de ficheros:
    @staticmethod # como no depende de nadie staticmethod
    def guardar_datos_v2(nomFich, datosFich):
        with open(nomFich,'wb') as fichero:
            pickle.dump(datosFich, fichero)

    # cargado de ficheros
    @staticmethod
    def cargar_datos_v2(nomFich):
        if not isinstance(nomFich, str):
            raise TypeError("Error: Nombre de fichero inválido.")
        with open(nomFich, 'rb') as fichero:
            datos = pickle.load(fichero)
        if not isinstance(datos, Hogar):
            raise Exception("Error: El fichero no contiene un hogar.")
        return datos


