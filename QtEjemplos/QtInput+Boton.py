import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QDialog, QLineEdit, QVBoxLayout
import sys

class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Escribe tu nombre!")
        # Creacion de widgets
        self.edit = QLineEdit()
        self.button = QPushButton("Mandalo!")
        # Colocamos los widgets y hacemos el layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Layout
        self.setLayout(layout)
        # Señal de boton clicado
        self.button.clicked.connect(self.saludos)

    def saludos(self):
        print(f"Hola {self.edit.text()}!")

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form (ventana)
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())