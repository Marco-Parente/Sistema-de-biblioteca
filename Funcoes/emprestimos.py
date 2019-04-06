import os
import csv
import datetime
import shutil


def iniciarEmprestimo():
    os.system("clear")
    print(" - Iniciar empréstimo - ")
    print("")
    print("Digite o ID do livro que será emprestado:")
    idLivro = input(" >> ")

    # Aqui devemos saber pelo cpf se o usuario existe ou nao
    print("Digite o CPF do usuario que esta solicitando o emprestimo:")
    cpf = input(" >> ")

    dataInicio = datetime.datetime.now().date()
    print("A data atual é: ", dataInicio.strftime("%d/%m/%Y"))

    dataMaximaEntrega = dataInicio + datetime.timedelta(days=7)
    print("A data maxima de entrega é: ",
          dataMaximaEntrega.strftime("%d/%m/%Y"))

    campos = ['ID', 'ID Livro', 'CPF', 'Inicio',
              'Maximo', 'Devolução', 'Qnt Renovação']

    Emprestimo = {
        'ID Livro': idLivro,
        'CPF': cpf,
        'Inicio': dataInicio.strftime("%d/%m/%Y"),
        'Maximo': dataMaximaEntrega.strftime("%d/%m/%Y"),
        'Devolução': '',
        'Qnt Renovação': 0
    }

    arquivoExiste = os.path.isfile("emprestimos.csv")

    if arquivoExiste:
        with open("emprestimos.csv", "r", newline="") as arquivo:
            leitor = csv.reader(arquivo)
            quantidadeEmprestimos = len(list(leitor))
            Emprestimo.update({"ID": quantidadeEmprestimos})
    else:
        Emprestimo.update({"ID": 1})

    with open("emprestimos.csv", "a", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        if not arquivoExiste:
            escritor.writeheader()

        if escritor.writerow(Emprestimo):
            print("Empréstimo realizado com sucesso.")


def renovarEmprestimo():
    os.system("clear")
    print(" - Renovar empréstimo - ")
    print("")

    campos = ['ID', 'ID Livro', 'CPF', 'Inicio',
              'Maximo', 'Devolução', 'Qnt Renovação']

    print("Emprestimos cuja data maxima foi extrapolada não são passíveis de renovação.")
    print("")
    print("As informações da tabela abaixo estão apresentadas da seguinte forma:")
    print("ID EMPRESTIMO | ESTADO DO EMPRESTIMO | CPF | DATA MAXIMA DE ENTREGA ATUAL")
    print("")

    empRenovaveis = []
    empTemporario = []

    arquivoExiste = os.path.isfile("emprestimos.csv")
    if not arquivoExiste:
        print("Arquivo nao encontrado")
    else:
        with open("emprestimos.csv", "r", newline="") as arquivo:
            next(arquivo)
            leitor = csv.reader(arquivo)
            print("Lista de todos os emprestimos em aberto:")
            for linhas in leitor:
                if linhas[5] == '':
                    diaMaximo = datetime.datetime.strptime(
                        linhas[4], "%d/%m/%Y").date()
                    if datetime.datetime.now().date() > diaMaximo:
                        print(linhas[0], "| extrapolado |",
                              linhas[2], "|", linhas[4])
                    else:
                        print(linhas[0], "|  renovável  |",
                              linhas[2], "|", linhas[4])
                        empRenovaveis.append(linhas)
        arquivo.close()

        print("")

        if not empRenovaveis:
            print("Nao há emprestimos para serem renovados")
            return
        else:
            print("Lista dos emprestimos que podem ser renovados:")
            for linhas in empRenovaveis:
                print(linhas[0], "|", linhas[2], "|", linhas[4])
            print("")
            idEmprestimo = -1
            while(idEmprestimo not in empRenovaveis[0]):
                print("Digite o ID do emprestimo que voce deseja renovar:")
                idEmprestimo = input(" >> ")

        with open("emprestimos.csv", "r", newline='') as arquivo:
            leitor = csv.DictReader(arquivo, fieldnames=campos)
            next(arquivo)
            for linha in leitor:
                if linha['ID'] == idEmprestimo:
                    # if linhacpf = aluno ou prof
                    # adicionar renovacao
                    dataNova = datetime.datetime.strptime(
                        linha['Maximo'], "%d/%m/%Y") + datetime.timedelta(7)
                    linha['Maximo'] = dataNova.strftime("%d/%m/%Y")
                    print("Nova data de entrega:", linha['Maximo'])
                empTemporario.append(linha)
            arquivo.close()

        with open("emprestimos.csv", "w", newline='') as arquivoTemporario:
            escritor = csv.DictWriter(arquivoTemporario, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(empTemporario)
            arquivoTemporario.close()

        shutil.move(arquivoTemporario.name, arquivo.name)
        print("Emprestimo renovado com sucesso!")
