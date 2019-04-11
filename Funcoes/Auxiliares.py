# Este arquivo tem como objetivo definir algumas funcoes (a maioria simples) que podem ser reusadas durante o codigo,
# envitando a repetição.
# Alem disso, a funcao listar livros emprestados por usuario se encontra aqui, pois e uma funcao comum à todas as outras

import os
import csv


def camposLivros():
    return ['ID', 'Titulo', 'Autor', 'Area', 'Paginas', 'Ano', 'Palavra 1', 'Palavra 2', 'Palavra 3', 'Emprestado']


def camposEmprestimos():
    return ['ID', 'ID Livro', 'CPF', 'Inicio', 'Maximo', 'Devolução', 'Qnt Renovação']


def camposUsuarios():
    return ['CPF', 'Nome', 'Tipo', 'Qnt Livros emprestados', 'Data p novo emprestimo']


def listarArquivo(nomeArquivo):
    lista = []

    arquivoExiste = os.path.isfile(nomeArquivo)

    if not arquivoExiste:
        return print("O arquivo ", nomeArquivo, " não existe, por isso, essa função nao pode ser utilizada.")

    with open(nomeArquivo, "r", newline='') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    arquivo.close()

    if not lista:
        return 0

    return lista


def listarUsuarios():
    return listarArquivo('usuarios.csv')


def listarEmprestimos():
    return listarArquivo('emprestimos.csv')


def listarLivros():
    return listarArquivo('livros.csv')
