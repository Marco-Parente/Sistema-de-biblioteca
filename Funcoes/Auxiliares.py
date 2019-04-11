# Este arquivo tem como objetivo definir algumas funcoes (a maioria simples) que podem ser reusadas durante o codigo,
# envitando a repetição.
# Alem disso, a funcao listar livros emprestados por usuario se encontra aqui, pois e uma funcao comum à todas as outras

import csv


def camposLivros():
    return ['ID', 'Titulo', 'Autor', 'Area', 'Paginas', 'Ano', 'Palavra 1', 'Palavra 2', 'Palavra 3', 'Emprestado']


def camposEmprestimos():
    return ['ID', 'ID Livro', 'CPF', 'Inicio', 'Maximo', 'Devolução', 'Qnt Renovação']


def camposUsuarios():
    return ['CPF', 'Nome', 'Tipo', 'Qnt Livros emprestados', 'Data p novo emprestimo']


def listarUsuarios():
    listaUsuarios = []
    with open("usuarios.csv", "r", newline='') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            listaUsuarios.append(linha)
    arquivo.close()

    if not listaUsuarios:
        return 0

    return listaUsuarios


def listarEmprestimos():
    listaEmprestimos = []
    with open("emprestimos.csv", "r", newline='') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            listaEmprestimos.append(linha)
    arquivo.close()

    if not listaEmprestimos:
        return 0

    return listaEmprestimos


def listarLivros():
    listaLivros = []
    with open("livros.csv", "r", newline='') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            listaLivros.append(linha)
    arquivo.close()

    if not listaLivros:
        return 0

    return listaLivros
