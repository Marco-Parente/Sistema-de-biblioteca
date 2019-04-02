
import os


def CadastrarNovoLivro():
    os.system("clear")
    print("Digite o título do livro: ")
    titulo = input(" >> ")
    print("Digite o autor do livro: ")
    autor = input(" >> ")
    print("Digite a area do livro: ")
    print("1. Ciencias da saude")
    print("2. Ciencias humanas")
    print("3. Ciencias sociais aplicadas")
    print("4. Engenharias")
    print("5. Linguistica")
    print("6. Letras e artes")
    print("7. Multidisciplinar")
    area = input(" >> ")
    print("Digite a quantidade de paginas: ")
    paginas = input(" >> ")
    print("Digite o ano do livro: ")
    ano = input(" >> ")
    print("Digite a primeira palavra chave: ")
    palavra1 = input(" >> ")
    print("Digite a segunda palavra chave: ")
    palavra2 = input(" >> ")
    print("Digite a terceiro palavra chave: ")
    palavra3 = input(" >> ")
    emprestado = False
