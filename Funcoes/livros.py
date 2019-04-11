
import os
import csv
import datetime
from .Auxiliares import *

# @fazerdps: arrumar os campos usando dict, verificar a insercao correta de dados, fechar arquivos


def selecionarArea():
    print("Digite a area do livro: ")
    print("")
    print("1. Ciencias da saude")
    print("2. Ciencias humanas")
    print("3. Ciencias sociais aplicadas")
    print("4. Engenharias")
    print("5. Linguistica")
    print("6. Letras e artes")
    print("7. Multidisciplinar")
    area = input(" >> ")
    if(area == "1"):
        area = "Ciencias da saude"
    elif(area == "2"):
        area = "Ciencias humanas"
    elif(area == "3"):
        area = "Ciencias sociais aplicadas"
    elif(area == "4"):
        area = "Engenharias"
    elif(area == "5"):
        area = "Linguistica"
    elif(area == "6"):
        area = "Letras e artes"
    elif(area == "7"):
        area = "Multidisciplinar"

    return area


def cadastrarNovoLivro():
    os.system("clear")
    print(" - Cadastrar livro - ")
    print("")
    Livro = {}

    print("Digite o título do livro: ")
    titulo = input(" >> ")
    Livro.update({"Titulo": titulo})
    print("Digite o autor do livro: ")
    autor = input(" >> ")
    Livro.update({"Autor": autor})

    area = selecionarArea()
    Livro.update({"Area": area})

    print("Digite a quantidade de paginas: ")
    paginas = input(" >> ")
    Livro.update({"Paginas": paginas})
    print("Digite o ano do livro: ")
    ano = input(" >> ")
    Livro.update({"Ano": ano})

    print("Digite a primeira palavra chave: ")
    palavra1 = input(" >> ")
    Livro.update({"Palavra 1": palavra1})
    print("Digite a segunda palavra chave: ")
    palavra2 = input(" >> ")
    Livro.update({"Palavra 2": palavra2})
    print("Digite a terceiro palavra chave: ")
    palavra3 = input(" >> ")
    Livro.update({"Palavra 3": palavra3})

    Livro.update({"Emprestado": False})

    arquivoExiste = os.path.isfile("livros.csv")

    if arquivoExiste:
        with open("livros.csv", "r", newline="") as arquivo:
            leitor = csv.reader(arquivo)
            quantidadeLivros = len(list(leitor))
            Livro.update({"ID": quantidadeLivros})
        arquivo.close()
    else:
        Livro.update({"ID": 1})

    with open("livros.csv", "a", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=camposLivros())

        if not arquivoExiste:
            escritor.writeheader()

        escritor.writerow(Livro)
    arquivo.close()


def buscarLivro():
    os.system("clear")
    print(" - Buscar livro - ")
    print("")
    print("Digite o critério de busca: ")
    print("1. Palavra-chave")
    print("2. Título")
    print("3. Autor")
    print("4. Área")
    criterio = input(" >> ")
    if(criterio == "1"):
        buscaLivroPalavraChave()
    elif(criterio == "2"):
        buscaLivroTitulo()
    elif(criterio == "3"):
        buscaLivroAutor()
    elif(criterio == "4"):
        buscaLivroArea()


def buscaLivroPalavraChave():
    os.system("clear")
    print(" - Busca por palavra-chave - ")
    print("")
    print("Digite a palavra-chave que deseja buscar:")
    palavra = input(" >> ")
    print("")

    encontrou = False
    livrosEncontrados = []

    with open("livros.csv", "r", newline="") as arquivo:
        next(arquivo)
        leitor = csv.reader(arquivo)
        for linhas in leitor:
            for x in range(6, 9):
                if linhas[x] == palavra:
                    encontrou = True
                    livrosEncontrados.append(linhas)
    arquivo.close()

    if not encontrou:
        print("Nenhum livro foi encontrado")
    else:
        print("Os seguintes livros foram encontrados: ")
        for livro in livrosEncontrados:
            print(livro[1])


def buscaLivroTitulo():
    os.system("clear")
    print(" - Busca por titulo - ")
    print("")
    print("Digite o titulo que deseja buscar:")
    titulo = input(" >> ")
    print("")

    encontrou = False
    livrosEncontrados = []

    with open("livros.csv", "r", newline="") as arquivo:
        next(arquivo)
        leitor = csv.reader(arquivo)
        for linhas in leitor:
            if linhas[1].find(titulo) >= 0:
                encontrou = True
                livrosEncontrados.append(linhas)
    arquivo.close()

    if not encontrou:
        print("Nenhum livro foi encontrado")
    else:
        print("Os seguintes livros foram encontrados: ")
        for livro in livrosEncontrados:
            print(livro[1])


def buscaLivroAutor():
    os.system("clear")
    print(" - Busca por autor - ")
    print("")
    print("Digite o autor que deseja buscar:")
    autor = input(" >> ")
    print("")

    encontrou = False
    livrosEncontrados = []

    with open("livros.csv", "r", newline="") as arquivo:
        next(arquivo)
        leitor = csv.reader(arquivo)
        for linhas in leitor:
            if linhas[2].find(autor) >= 0:
                encontrou = True
                livrosEncontrados.append(linhas)
    arquivo.close()

    if not encontrou:
        print("Nenhum livro foi encontrado")
    else:
        print("Os seguintes livros foram encontrados: ")
        for livro in livrosEncontrados:
            print(livro[1])


def buscaLivroArea():
    os.system("clear")
    print(" - Busca por área - ")
    print("")
    area = selecionarArea()
    print("")

    encontrou = False
    livrosEncontrados = []

    with open("livros.csv", "r", newline="") as arquivo:
        next(arquivo)
        leitor = csv.reader(arquivo)
        for linhas in leitor:
            if linhas[3] == area:
                encontrou = True
                livrosEncontrados.append(linhas)
    arquivo.close()

    if not encontrou:
        print("Nenhum livro foi encontrado")
    else:
        print("Os seguintes livros foram encontrados: ")
        for livro in livrosEncontrados:
            print(livro[1])


def livrosEmprestadosUsuario():
    os.system("clear")
    print(" - Livros emprestados em determinado periodo de tempo - ")
    print("")

    listaEmprestimos = listarEmprestimos()
    listaLivros = listarLivros()
    listaUsuarios = listarUsuarios()

    if not listaEmprestimos:
        return
    if not listaLivros:
        return
    if not listaUsuarios:
        return

    print("Para começar, digite a data inicial da busca (FORMATO: DD/MM/AAAA):")
    dia = input("Dia: ")
    mes = input("Mes: ")
    ano = input("Ano: ")
    dataInicial = datetime.datetime.strptime(
        dia+'/'+mes+'/'+ano, "%d/%m/%Y").date()
    print("")

    print("Agora, digite a data final da busca (FORMATO: DD/MM/AAAA):")
    diaFim = input("Dia: ")
    mesFim = input("Mes: ")
    anoFim = input("Ano: ")
    dataFinal = datetime.datetime.strptime(
        diaFim+'/'+mesFim+'/'+anoFim, "%d/%m/%Y").date()
    print("")

    emprestimosNaData = []
    for emprestimo in listaEmprestimos:
        empDataInicial = datetime.datetime.strptime(
            emprestimo['Inicio'], "%d/%m/%Y").date()
        if dataInicial <= empDataInicial:
            if not emprestimo['Devolução']:
                emprestimosNaData.append(emprestimo)
            else:
                empDataFinal = datetime.datetime.strptime(
                    emprestimo['Devolução'], "%d/%m/%Y").date()
                if dataFinal >= empDataFinal:
                    emprestimosNaData.append(emprestimo)

    listaCPFs = []
    listaIDLivros = []
    for emprestimos in emprestimosNaData:
        listaCPFs.append(emprestimo['CPF'])
        listaIDLivros.append(emprestimo['ID Livro'])

    infoLivros = []
    for livro in listaLivros:
        if any(idNaData == livro['ID'] for idNaData in listaIDLivros):
            infoLivros.append(livro)

    infoUsuarios = []
    for usuario in listaUsuarios:
        if any(cpfNaData == usuario['CPF'] for cpfNaData in listaCPFs):
            infoUsuarios.append(usuario)

    print("Nesse intervalo de tempo, foram encontrados os seguintes resultados:")
    for emprestimo in emprestimosNaData:
        livroS = next(
            livro for livro in infoLivros if livro['ID'] == emprestimo['ID Livro'])
        usuarioS = next(
            usuario for usuario in infoUsuarios if usuario['CPF'] == emprestimo['CPF'])
        print("-------")
        print("ID do emprestimo:", emprestimo['ID'])
        print("Livro:", livroS['Titulo'])
        print("CPF:", usuarioS['CPF'], "| Nome:", usuarioS['Nome'])
        if not emprestimo['Devolução']:
            print('O livro ainda nao foi devolvido.')
        else:
            print('Devolvido em:', emprestimo['Devolução'])
