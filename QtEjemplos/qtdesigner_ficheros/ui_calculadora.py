# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(220, 265, 121, 31))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(220, 305, 121, 31))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(220, 345, 121, 31))
        self.labelResultado = QLabel(self.centralwidget)
        self.labelResultado.setObjectName(u"labelResultado")
        self.labelResultado.setGeometry(QRect(70, 340, 141, 31))
        font = QFont()
        font.setPointSize(22)
        self.labelResultado.setFont(font)
        self.labelResultado.setFrameShape(QFrame.Shape.StyledPanel)
        self.labelNum2 = QLabel(self.centralwidget)
        self.labelNum2.setObjectName(u"labelNum2")
        self.labelNum2.setGeometry(QRect(80, 300, 131, 31))
        self.labelNum2.setFont(font)
        self.labelNum2.setFrameShape(QFrame.Shape.StyledPanel)
        self.labelNum1 = QLabel(self.centralwidget)
        self.labelNum1.setObjectName(u"labelNum1")
        self.labelNum1.setGeometry(QRect(80, 260, 131, 31))
        self.labelNum1.setFont(font)
        self.labelNum1.setFrameShape(QFrame.Shape.StyledPanel)
        self.pushButtonSumar = QPushButton(self.centralwidget)
        self.pushButtonSumar.setObjectName(u"pushButtonSumar")
        self.pushButtonSumar.setGeometry(QRect(360, 295, 161, 61))
        font1 = QFont()
        font1.setPointSize(26)
        font1.setBold(True)
        font1.setUnderline(True)
        self.pushButtonSumar.setFont(font1)
        self.pushButtonSalir = QPushButton(self.centralwidget)
        self.pushButtonSalir.setObjectName(u"pushButtonSalir")
        self.pushButtonSalir.setGeometry(QRect(240, 430, 81, 26))
        font2 = QFont()
        font2.setPointSize(20)
        self.pushButtonSalir.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora Epica", None))
        self.labelResultado.setText(QCoreApplication.translate("MainWindow", u"Resultado", None))
        self.labelNum2.setText(QCoreApplication.translate("MainWindow", u"Num 2", None))
        self.labelNum1.setText(QCoreApplication.translate("MainWindow", u"Num 1", None))
        self.pushButtonSumar.setText(QCoreApplication.translate("MainWindow", u"Sumalos!", None))
        self.pushButtonSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

