import os
import csv
import datetime
import shutil
from tempfile import NamedTemporaryFile


def isIndicenaLista(lst, indice, valor):
    for i, dic in enumerate(lst):
        if dic[indice] == valor:
            return True
    return False

# def iIL(lst, indice, valor):
#     return if any(  )


def iniciarEmprestimo():
    os.system("clear")
    print(" - Iniciar empréstimo - ")
    print("")

    listaLivros = []
    livrosDisponiveis = []

    with open("livros.csv", "r", newline='') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            listaLivros.append(linha)
            if linha['Emprestado'] == 'False':
                livrosDisponiveis.append(linha)
    arquivo.close()

    if not livrosDisponiveis:
        print("Não há livros disponíveis para empréstimo.")
        return

    print("Os seguintes livros estão disponíveis para empréstimo:")
    for livro in livrosDisponiveis:
        print("ID do livro:", livro['ID'], "| Titulo do livro:",
              livro['Titulo'], "| Ano do livro:", livro['Ano'])

    print("")

    idLivro = '-1'

    while not isIndicenaLista(livrosDisponiveis, 'ID', idLivro):
        print("Digite o ID do livro que será emprestado:")
        idLivro = input(" >> ")

    livroSelecionado = next(
        livro for livro in livrosDisponiveis if livro['ID'] == idLivro)

    # TODO Aqui devemos saber pelo cpf se o usuario existe ou nao
    print("Digite o CPF do usuario que esta solicitando o emprestimo:")
    cpf = input(" >> ")

    dataInicio = datetime.datetime.now().date()
    print("A data atual é: ", dataInicio.strftime("%d/%m/%Y"))

    dataMaximaEntrega = dataInicio + datetime.timedelta(days=7)
    print("A data maxima de entrega é: ",
          dataMaximaEntrega.strftime("%d/%m/%Y"))

    campos = ['ID', 'ID Livro', 'CPF', 'Inicio',
              'Maximo', 'Devolução', 'Qnt Renovação']

    camposLivros = ['ID', 'Titulo', 'Autor', 'Area', 'Paginas', 'Ano',
                    'Palavra 1', 'Palavra 2', 'Palavra 3', 'Emprestado']

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

    livroSelecionado['Emprestado'] = True

    for livro in listaLivros:
        if livro['ID'] == livroSelecionado['ID']:
            livro = livroSelecionado

    with open("livros.csv", "w", newline='') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=camposLivros)
        escritor.writeheader()
        escritor.writerows(listaLivros)
    arquivo.close()


def renovarEmprestimo():
    os.system("clear")
    print(" - Renovar empréstimo - ")
    print("")

    campos = ['ID', 'ID Livro', 'CPF', 'Inicio',
              'Maximo', 'Devolução', 'Qnt Renovação']

    print("Emprestimos cuja data maxima foi extrapolada não são passíveis de renovação.")
    print("")
    print("As informações da tabela abaixo estão apresentadas da seguinte forma:")
    print("ID emprestimo | Estado do emprestimo | CPF | Qnt. renovação atual | Data maxima de entrega atual")
    print("")

    empRenovaveis = []
    empTemporario = []

    arquivoExiste = os.path.isfile("emprestimos.csv")
    if not arquivoExiste:
        print("Arquivo nao encontrado")
    else:
        with open("emprestimos.csv", "r", newline="") as arquivo:
            leitor = csv.reader(arquivo)
            next(arquivo)
            print("Lista de todos os emprestimos em aberto:")
            for linhas in leitor:
                if linhas[5] == '':
                    diaMaximo = datetime.datetime.strptime(
                        linhas[4], "%d/%m/%Y").date()
                    if datetime.datetime.now().date() > diaMaximo:
                        print(linhas[0], "|     extrapolado     |",
                              linhas[2], "|", linhas[6], "|", linhas[4])
                    elif int(linhas[6]) >= 2:
                        print(linhas[0], "| limite indisponivel |",
                              linhas[2], "|", linhas[6], "|", linhas[4])
                    else:
                        print(linhas[0], "|      renovável      |",
                              linhas[2], "|", linhas[6], "|",  linhas[4])
                        empRenovaveis.append(linhas)
        arquivo.close()

        print("")
        idEmprestimo = 0
        if not empRenovaveis:
            print("Nao há emprestimos para serem renovados")
            return
        else:
            print("Lista dos emprestimos que podem ser renovados:")
            for linhas in empRenovaveis:
                print(linhas[0], "|", linhas[2],
                      "|", linhas[4], "|", linhas[6])
            print("")
            while(idEmprestimo not in empRenovaveis[0]):
                print("Digite o ID do empréstimo que voce deseja renovar:")
                idEmprestimo = input(" >> ")

        with open("emprestimos.csv", "r", newline='') as arquivo:
            leitor = csv.DictReader(arquivo, fieldnames=campos)
            next(arquivo)
            for emprestimo in leitor:
                if emprestimo['ID'] == idEmprestimo:
                    # if emprestimocpf = aluno ou prof
                    dataNova = datetime.datetime.strptime(
                        emprestimo['Maximo'], "%d/%m/%Y") + datetime.timedelta(7)
                    emprestimo['Maximo'] = dataNova.strftime("%d/%m/%Y")
                    emprestimo['Qnt Renovação'] = int(
                        emprestimo['Qnt Renovação']) + 1
                    print("Nova data de entrega:", emprestimo['Maximo'])
                empTemporario.append(emprestimo)
            arquivo.close()

        with open("emprestimos.csv", "w", newline='') as arquivoTemporario:
            escritor = csv.DictWriter(arquivoTemporario, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(empTemporario)
            arquivoTemporario.close()

        shutil.move(arquivoTemporario.name, arquivo.name)
        print("Emprestimo renovado com sucesso!")


def encerrarEmprestimo():
    os.system("clear")
    print(" - Encerrar empréstimo - ")
    print("")

    campos = ['ID', 'ID Livro', 'CPF', 'Inicio',
              'Maximo', 'Devolução', 'Qnt Renovação']

    empTodos = []
    empAbertos = []

    arquivoExiste = os.path.isfile("emprestimos.csv")
    if not arquivoExiste:
        print("Nenhum arquivo de emprestimos foi encontrado.")
        return
    else:
        with open("emprestimos.csv", "r", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)
            for emprestimo in leitor:
                empTodos.append(emprestimo)
                if not emprestimo['Devolução']:
                    empAbertos.append(emprestimo)

    arquivo.close()

    if not empAbertos:
        print("Não há empréstimos para se encerrar.")
        return

    print("Lista de todos os empréstimos em aberto:")
    for emprestimo in empAbertos:
        print("ID:", emprestimo['ID'], "| CPF:", emprestimo['CPF'],
              "| Data limite de entrega:", emprestimo['Maximo'])

    escolha = -1

    while(not any(emprestimo['ID'] == escolha for emprestimo in empAbertos)):
        print("Digite o ID do emprestimo a ser encerrado: ")
        escolha = input(" >> ")

    emprestimoSelecionado = next(
        emprestimo for emprestimo in empAbertos if emprestimo['ID'] == escolha)

    devolucao = datetime.datetime.now()
    emprestimoSelecionado['Devolução'] = devolucao.strftime("%d/%m/%Y")
    dataMaxima = datetime.datetime.strptime(
        emprestimoSelecionado['Maximo'], "%d/%m/%Y")

    diasAtraso = (devolucao - dataMaxima).days

    diasAtraso = 0 if diasAtraso <= 0 else diasAtraso

    punicao = diasAtraso*2
    print(empTodos)

    print("")

    print("A data de entrega máxima é:", emprestimoSelecionado['Maximo'])
    print("A data em que o livro está sendo devolvido é:",
          emprestimoSelecionado['Devolução'])
    print("")
    if diasAtraso:
        print("O livro foi entregado com", diasAtraso, "dias de atraso.")
        print("Uma punição de", punicao, "dias será aplicada ao usuario.")
    else:
        print("O livro foi entregado sem atrasos.")

    with open("emprestimos.csv", "w", newline='') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(empTodos)
    arquivo.close()

    camposLivros = ['ID', 'Titulo', 'Autor', 'Area', 'Paginas', 'Ano',
                    'Palavra 1', 'Palavra 2', 'Palavra 3', 'Emprestado']

    arquivoLivro = "livros.csv"
    arquivoTemp = NamedTemporaryFile(mode="w", delete="false")

    with open(arquivoLivro, "r", newline='') as arquivo, arquivoTemp:
        leitor = csv.DictReader(arquivo, fieldnames=camposLivros)
        escritor = csv.DictWriter(arquivoTemp, fieldnames=camposLivros)
        for livro in leitor:
            if livro['ID'] == emprestimoSelecionado['ID Livro']:
                livro['Emprestado'] = False
            escritor.writerow(livro)
    arquivo.close()
    arquivoTemp.close()
    shutil.move(arquivoTemp.name, arquivoLivro)
