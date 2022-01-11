from PyQt5 import uic, QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='lojinha_ze'
)

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    print('Produto:', linha1)
    print('Preço:', linha2)
    print('CPF:', linha3)

    cursor = banco.cursor()
    comando_SQL = 'INSERT INTO lojinha_ze (produto, preco, cpf) VALUES (%s,%s,%s)'
    dados = (str(linha1), str(linha2), str(linha3))
    cursor.execute(comando_SQL, dados)
    banco.commit()

    #Limpar os dados após o envio.
    formulario.lineEdit.setText('')
    formulario.lineEdit_2.setText('')
    formulario.lineEdit_3.setText('')

#Cria a aplicação
app = QtWidgets.QApplication([])
#Carregar o arquivo 'ui'
formulario = uic.loadUi('untitled.ui')
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
