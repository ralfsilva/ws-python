from PyQt5 import uic, QtWidgets

def calc():
    num1 = int(calculadora.lineEdit_num1.text())
    num2 = int(calculadora.lineEdit_num2.text())

    operacao = input("Digite qual operação vai ser feita: ")

    if operacao == calculadora.lineEdit_operacao.text('+'):
        print (num1 + num2)

    elif operacao == '-':
        print (num1 - num2)

    elif operacao == '*':
        print (num1 * num2)

    elif operacao == '/':
        print (num1 / num2)

app = QtWidgets.QApplication([])
calculadora = uic.loadUi("calculadora.ui")
calculadora.pb_calcular.clicked.connect(calc)
calculadora.show()
app.exec()