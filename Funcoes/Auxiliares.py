def camposLivros():
    return ['ID', 'Titulo', 'Autor', 'Area', 'Paginas', 'Ano', 'Palavra 1', 'Palavra 2', 'Palavra 3', 'Emprestado']


def camposEmprestimos():
    return ['ID', 'ID Livro', 'CPF', 'Inicio', 'Maximo', 'Devolução', 'Qnt Renovação']


def camposUsuarios():
    return ['CPF', 'Nome', 'Tipo', 'Qnt Livros emprestados', 'Data p novo emprestimo']
