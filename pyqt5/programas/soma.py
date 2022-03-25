from PyQt5 import uic, QtWidgets

def soma():
    num1 = int(form_soma.lineEdit_num1.text())
    num2 = int(form_soma.lineEdit_num2.text())
    print (num1+num2)

app = QtWidgets.QApplication([])
form_soma = uic.loadUi("form_soma.ui")
form_soma.pb_calcular.clicked.connect(soma)
form_soma.show()
app.exec()
