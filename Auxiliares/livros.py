
import os
import csv


def cadastrarNovoLivro():
    os.system("clear")

    Livro = {}

    print("Digite o título do livro: ")
    titulo = input(" >> ")
    Livro.update({"Titulo": titulo})
    print("Digite o autor do livro: ")
    autor = input(" >> ")
    Livro.update({"Autor": autor})

    print("Digite a area do livro: ")
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

    arquivoExiste = os.path.isfile("teste.csv")

    if arquivoExiste:
        with open("teste.csv", "r", newline="") as arquivo:
            leitor = csv.reader(arquivo)
            quantidadeLivros = len(list(leitor))
            Livro.update({"ID": quantidadeLivros})
    else:
        Livro.update({"ID": 1})

    with open("teste.csv", "a", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        if not arquivoExiste:
            escritor.writeheader()

        escritor.writerow(Livro)
