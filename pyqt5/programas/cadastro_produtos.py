from PyQt5 import uic, QtWidgets

def main():
    codigo = form.codigo_lineEdit.text()
    descricao = form.descricao_lineEdit.text()
    preco = form.preco_lineEdit.text()

    if form.informatica_radioButton.isChecked():
        print ("Categoria: Informática")
    elif form.alimentos_radioButton.isChecked():
        print ("Categoria: Alimentos")
    elif form.eletronicos_radioButton.isChecked():
        print ("Categoria: Eletrônicos")

    print("Código: ",codigo)
    print("Descrição: ",descricao)
    print("Preço: R$ ",preco)


app = QtWidgets.QApplication([])
form = uic.loadUi("form_cadastro_produtos.ui")
form.enviar_pb.clicked.connect(main)
form.show()
app.exec()
