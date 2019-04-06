import os
import csv
import datetime


def iniciarEmprestimo():
    os.system("clear")
    print(" - Iniciar empréstimo - ")
    print("")
    Emprestimo = {}
    # print("Digite o ID do livro que será emprestado:")
    # IDLivro = input(" >> ")

    # # Aqui devemos saber pelo cpf se o usuario existe ou nao
    # print("Digite o CPF do usuario que esta solicitando o emprestimo:")
    # CPFUsuario = input(" >> ")

    dataInicio = datetime.datetime.now()
    print("A data atual é: ", dataInicio.day, "/",
          dataInicio.month, "/", dataInicio.year, sep='')

    dataMaximaEntrega = dataInicio + datetime.timedelta(days=7)
    print("A data maxima de entrega é: ", dataMaximaEntrega.day, "/",
          dataMaximaEntrega.month, "/", dataMaximaEntrega.year, sep='')

    campos = ['ID', 'ID Livro', 'CPF', 'Inicio', 'Maximo', 'Devolução',
              'Qnt Renovação']

    # Isso aqui ta errado, arrumar dps
    Emprestimo.update({"Inicio": dataInicio}, {"Maximo": dataMaximaEntrega})
    print(Emprestimo)
