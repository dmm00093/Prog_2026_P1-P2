import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QDialog, QLineEdit, QVBoxLayout, QMainWindow
from qtdesigner_ficheros.ui_calculadora import Ui_MainWindow

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonSumar.clicked.connect(self.ButtonSumarHandler)
        self.ui.pushButtonSalir.clicked.connect(self.ButtonSalirHandler)

    @Slot()
    def ButtonSumarHandler(self):
        num1 = float(self.ui.lineEdit.text())
        num2 = float(self.ui.lineEdit_2.text())
        res = num1 + num2
        self.ui.lineEdit_3.setText(str(res))

    @Slot()
    def ButtonSalirHandler(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec())
