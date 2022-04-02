from PyQt5 import uic, QtWidgets

def calc():
    num1 = int(cal.lineEdit_num1.text())
    num2 = int(cal.lineEdit_num2.text())

    operacao = cal.lineEdit_operacao.text()

    if operacao == '+':
        print ("Soma entre {} e {}: {}".format(num1, num2 (num1 + num2)))

    elif operacao == '-':
        print ("Subtração entre {} e {}: {}".format(num1, num2, (num1 - num2)))

    elif operacao == '*':
        print ("Multiplicação entre {} e {}: {}".format(num1, num2, (num1 * num2)))

    elif operacao == '/':

        print ("Divisão entre {} e {}: {}".format(num1, num2, float(num1 / num2)))

app = QtWidgets.QApplication([])
cal = uic.loadUi("calculadora.ui")
cal.pb_calcular.clicked.connect(calc)
cal.show()
app.exec()