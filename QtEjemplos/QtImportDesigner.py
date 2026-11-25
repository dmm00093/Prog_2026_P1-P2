import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Slot, QFile
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QDialog, QLineEdit, QVBoxLayout, QMainWindow
from qtdesigner_ficheros.ui_test import Ui_MainWindow
import sys

class MainWindow(QMainWindow): # FUNCIONALIDAD INTERFAZ, VENTANA PRINCIPAL
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() # DEFINICION INTERFAZ CREADA EN QtDESIGNER
        self.ui.setupUi(self)
        # ADICION DE FUNCIONALIDAD EXTRA (CONEXION SEÑALES CON SU RANURA)
        self.ui.checkBox.clicked.connect(self.ok_handler)

    @Slot() # RANURA (SLOT)
    def ok_handler(self):
        print("Hola!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())