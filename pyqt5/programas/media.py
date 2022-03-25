from PyQt5 import uic, QtWidgets

def mediano():
    nome = med.lineEdit_nome.text()

    nota1 = float(med.lineEdit_nota1.text())
    nota2 = float(med.lineEdit_nota2.text())
    nota3 = float(med.lineEdit_nota3.text())

    notas = (nota1 + nota2 + nota3) / 3

    if notas >= 7.0 and notas <= 10.0:
        print (f'{nome} sua média foi {notas:.2f} e você foi Aprovado (a).')

    elif notas >= 0.0 and notas < 7.0:
        print (f'{nome} sua média foi {notas:.2f} e você foi Reprovado (a).')


app = QtWidgets.QApplication([])
med = uic.loadUi("media.ui")
med.pb_calcular.clicked.connect(mediano)
med.show()
app.exec()