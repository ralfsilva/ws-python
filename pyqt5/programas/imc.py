import sys
import math
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
from PyQt5 import uic, QtWidgets

def indice():
    grau = 0

    altura = float(massa.lineEdit_altura.text())
    peso = float(massa.lineEdit_peso.text())

    calculo_imc = (peso / math.pow(altura, 2))

    if calculo_imc < 18.5:
        massa.widget_magreza.setStyleSheet('background-color: #ebfdea;')        
    elif calculo_imc >= 18.5 and calculo_imc < 25.0:
        massa.widget_normal.setStyleSheet('background-color: #ebfdea;')
    elif calculo_imc >= 25.0 and calculo_imc < 30.0:
        grau = 1
        massa.widget_sobrepeso.setStyleSheet('background-color: #ebfdea;')
    elif calculo_imc >= 30.0 and calculo_imc < 40.0:
        grau = 2
        massa.widget_obesidade.setStyleSheet('background-color: #ebfdea;')
    elif calculo_imc >= 40.0:
        massa.widget_obesidade_grave.setStyleSheet('background-color: #ebfdea;')

    calculo_imc = round(calculo_imc, 2)
    calc = str(calculo_imc)
    massa.label_imc.setText(calc)
    
    massa.pb_limpar.clicked.connect(massa.label_imc.clear)
    
    #Lógica incompleta para apagar background verde-claro
    
    #massa.widget_sobrepeso.setStyleSheet('background-color: transparent; border-bottom: 3px solid #e7eaee;')



app = QtWidgets.QApplication([])
massa = uic.loadUi("gui_imc.ui")
massa.pb_calcular.clicked.connect(indice)
massa.pb_limpar.clicked.connect(indice)
massa.show()
app.exec()