
import os
import csv

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

    campos = ['ID', 'Titulo', 'Autor', 'Area', 'Paginas', 'Ano',
              'Palavra 1', 'Palavra 2', 'Palavra 3', 'Emprestado']

    arquivoExiste = os.path.isfile("livros.csv")

    if arquivoExiste:
        with open("livros.csv", "r", newline="") as arquivo:
            leitor = csv.reader(arquivo)
            quantidadeLivros = len(list(leitor))
            Livro.update({"ID": quantidadeLivros})
    else:
        Livro.update({"ID": 1})

    with open("livros.csv", "a", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        if not arquivoExiste:
            escritor.writeheader()

        escritor.writerow(Livro)


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

    if not encontrou:
        print("Nenhum livro foi encontrado")
    else:
        print("Os seguintes livros foram encontrados: ")
        for livro in livrosEncontrados:
            print(livro[1])
