import os
from .livros import *
from .emprestimos import *
from .usuarios import *


def menuPrincipal():
    os.system('clear')
    print("Bem vindo ao sistema bibliotecário")
    print("")
    print("Escolha o que deseja fazer:")
    print("1. Sistema de usuários.")
    print("2. Sistema de empréstimos.")
    print("3. Sistema de livros.")
    print("0. Encerrar sistema.")
    choice = int(input('>> '))
    execMenuPrincipalChoice(choice)


def execMenuPrincipalChoice(choice):
    while True:
        if choice == 1:
            menuUsuarios()
        elif choice == 2:
            menuEmprestimos()
        elif choice == 3:
            menuLivros()
        elif choice == 0:
            os.system("clear")
            print("Obrigado por utilizar o nosso sistema :}")
            exit()
        else:
            input('Opção inválida, aperte enter e digite novamente... ')
            break


def execMenuUsuario(choice):
    while True:
        if choice == 1:
            CadastrarNovoUsuario()
            input('Aperte enter para continuar... ')
            menuUsuarios()
        elif choice == 2:
            AtualizarUsuario()
            input('Aperte enter para continuar... ')
            menuUsuarios()
        elif choice == 3:
            BuscarUsuario()
            input('Aperte enter para continuar... ')
            menuUsuarios()
        elif choice == 0:
            menuPrincipal()
        else:
            input('Opção inválida, aperte enter e digite novamente... ')
            break


def execMenuEmprestimos(choice):
    while True:
        if choice == 1:
            iniciarEmprestimo()
            input('Aperte enter para continuar... ')
            menuEmprestimos()
        elif choice == 2:
            renovarEmprestimo()
            input('Aperte enter para continuar... ')
            menuEmprestimos()
        elif choice == 3:
            encerrarEmprestimo()
            input('Aperte enter para continuar... ')
            menuEmprestimos()
        elif choice == 0:
            menuPrincipal()
        else:
            input('Opção inválida, aperte enter e digite novamente... ')
            break


def execMenuLivro(choice):
    while True:
        if choice == 1:
            cadastrarNovoLivro()
            input('Aperte enter para continuar... ')
            menuLivros()
        elif choice == 2:
            livrosEmprestadosUsuario()
            input('Aperte enter para continuar... ')
            menuLivros()
        elif choice == 3:
            buscarLivro()
            input('Aperte enter para continuar... ')
            menuLivros()
        elif choice == 0:
            menuPrincipal()
        else:
            input('Opção inválida, aperte enter e digite novamente... ')
            break


def menuUsuarios():
    os.system('clear')
    print("- Usuários -")
    print("")
    print("Escolha o que deseja fazer:")
    print("1. Cadastrar usuário.")
    print("2. Atualizar usuário.")
    print("3. Buscar usuário")
    print("0. Voltar.")
    subChoice = int(input(" >> "))
    execMenuUsuario(subChoice)


def menuLivros():
    os.system('clear')
    print("- Livros -")
    print("")
    print("Escolha o que deseja fazer:")
    print("1. Cadastrar novo livro.")
    print("2. Listar livros que foram ou estão emprestados a um determinado usuario em determinado periodo de tempo.")
    print("3. Buscar livro.")
    print("0. Voltar.")
    subChoice = int(input(" >> "))
    execMenuLivro(subChoice)


def menuEmprestimos():
    os.system('clear')
    print("- Emprestimos -")
    print("")
    print("Escolha o que deseja fazer:")
    print("1. Iniciar empréstimo.")
    print("2. Renovar emprestimo.")
    print("3. Encerrar empréstimo.")
    print("0. Voltar.")
    subChoice = int(input(" >> "))
    execMenuEmprestimos(subChoice)


if __name__ == '__main__':
    while True:
        menuPrincipal()
