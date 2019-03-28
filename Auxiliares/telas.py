#coding: utf-8

import sys
import os


def menuPrincipal():
    os.system('clear')
    print("\nBem vindo ao sistema bibliotecário")
    print("Escolha o que deseja fazer:")
    print("1. Sistema de usuários.")
    print("2. Sistema de empréstimos.")
    print("3. Sistema de livros.")
    print("0. Encerrar sistema.")
    choice = input(" >> ")
    execMenu(choice)


def menuLivros():
    os.system('clear')
    print("- Livros -")
    print("Escolha o que deseja fazer:")
    print("1. Cadastrar novo livro.")
    print("2. Listar livros emprestados por um usuario em determinado tempo.")
    print("3. Buscar livro.")
    print("0. Voltar.")
    subChoice = input(" >> ")
    execSubMenu(subChoice)


def menuEmprestimos():
    os.system('clear')
    print("- Emprestimos -")
    print("Escolha o que deseja fazer:")
    print("1. Iniciar empréstimo.")
    print("2. Renovar emprestimo.")
    print("3. Encerrar empréstimo.")
    print("4. Listar livros emprestados por um usuario em determinado tempo.")
    print("0. Voltar.")
    subChoice = input(" >> ")
    execSubMenu(subChoice)


def menuUsuarios():
    os.system('clear')
    print("- Usuários -")
    print("Escolha o que deseja fazer:")
    print("1. Cadastrar usuário.")
    print("2. Atualizar usuário.")
    print("3. Listar livros emprestados por um usuario em determinado tempo.")
    print("4. Buscar usuário")
    print("0. Voltar.")
    subChoice = input(" >> ")
    execSubMenu(subChoice)


def desligarSistema():
    os.system('clear')
    print('Obrigado por utilizar o nosso sistema! :}')


acoesPrincipais = {
    '1': {
        'iniciar': menuUsuarios,
        '0': menuPrincipal
    },
    '2': {
        'iniciar': menuEmprestimos,
        '0': menuPrincipal
    },
    '3': {
        'iniciar': menuLivros,
        '0': menuPrincipal
    },
    '0': {
        'iniciar': desligarSistema
    }
}


def execMenu(choice):
    try:
        acoesPrincipais[choice]['iniciar']()
    except KeyError:
        print("Opção inválida, tente denovo.")


def execSubMenu(choice):
    try:
        acoesPrincipais[choice]['iniciar']()
    except KeyError:
        print("Opção inválida, tente denovo.")
        subChoice = input(" >> ")
        execSubMenu(subChoice)


menuPrincipal()
