import os
import csv
from .Auxiliares import *


def estaNaLista(lst, indice, valor):
    for item in lst:
        if item[indice] == valor:
            return True
    return False


def CadastrarNovoUsuario():
    os.system("clear")
    print(" - Cadastrar Usuario - ")
    print("")
    Usuario = {}
    print("O usuário é Discente ou Docente?")
    resposta = input(" >> ")
    if resposta.upper() == "DISCENTE":
        Usuario.update({"Tipo": resposta})
    elif resposta.upper() == "DOCENTE":
        Usuario.update({"Tipo": resposta})
    else:
        input('Resposta inválida. Pressione enter e digite novamente...')
        CadastrarNovoUsuario()
    print("Digite seu CPF:")
    CPF = input(" >> ")
    Usuario.update({"CPF": CPF})
    print("Digite seu nome:")
    Nome = input(" >> ")
    Usuario.update({"Nome": Nome})
    Usuario.update({"Qnt Livros emprestados": 0})
    Usuario.update({"Data p novo emprestimo": ""})

    arquivoExiste = os.path.isfile("usuarios.csv")

    with open("usuarios.csv", "a", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=camposUsuarios())
        if not arquivoExiste:
            escritor.writeheader()

        escritor.writerow(Usuario)
    arquivo.close()


def AtualizarUsuario():
    os.system("clear")
    print(" - Atualizar Usuario - ")
    print("")
    listaUsuarios = listarUsuarios()
    escolha = 0

    if not listaUsuarios:
        print("Nenhum usuário foi encontrado.")
        return

    for usuario in listaUsuarios:
        print('Nome:', usuario['Nome'], '| CPF:', usuario['CPF'])

    print("Selecione o usuario que você deseja atualizar pelo CPF:")
    cpfEscolhido = input(" >> ")

    while not estaNaLista(listaUsuarios, 'CPF', cpfEscolhido):
        print("CPF nao encontrado na lista, você tem certeza de que digitou certo? Tente novamente.")
        cpfEscolhido = input(" >> ")

    usuarioSelecionado = next(
        usuario for usuario in listaUsuarios if usuario['CPF'] == cpfEscolhido)

    print("Por questões de segurança, não é permitido a alteração da quantidade de livros emprestados e a punição aplicada ao usuário. ")
    print("Essas são as informações do usuário selecionado que são passíveis de alteração:")
    print("Nome:", usuarioSelecionado['Nome'], "| CPF:",
          usuarioSelecionado['CPF'], "| Tipo:", usuarioSelecionado['Tipo'])

    while escolha < 1 or escolha > 3:
        print("Escolha qual campo você deseja alterar:")
        print("[1] - Nome")
        print("[2] - CPF")
        print("[3] - Tipo")
        escolha = int(input(" >> "))

    if escolha == 1:
        print("Digite o novo nome do usuario: ")
        usuarioSelecionado['Nome'] = input(" >> ")
    elif escolha == 2:
        print("Digite o novo CPF do usuario")
        usuarioSelecionado['CPF'] = input(" >> ")
    else:
        print('O usuario possuia o tipo:', usuarioSelecionado['Tipo'])
        if usuarioSelecionado['Tipo'].upper() == "DOCENTE":
            usuarioSelecionado['Tipo'] = "Discente"
        else:
            usuarioSelecionado['Tipo'] = "Docente"
        print('Agora ele possui o tipo:', usuarioSelecionado['Tipo'])

    with open("usuarios.csv", "w", newline='') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=camposUsuarios())
        escritor.writeheader()
        escritor.writerows(listaUsuarios)
    arquivo.close()


def BuscarUsuario():
    os.system("clear")
    print(" - Buscar Usuario - ")
    print("")
    listaUsuarios = listarUsuarios()

    if not listaUsuarios:
        print("Não há usuários cadastrados no sistema.")
        return

    for usuario in listaUsuarios:
        print('Nome:', usuario['Nome'], '| CPF:', usuario['CPF'])

    print("Selecione o usuario que você deseja saber mais informações pelo CPF:")
    cpfEscolhido = input(" >> ")

    while not estaNaLista(listaUsuarios, 'CPF', cpfEscolhido):
        print("CPF nao encontrado na lista, você tem certeza de que digitou certo? Tente novamente.")
        cpfEscolhido = input(" >> ")

    usuarioSelecionado = next(
        usuario for usuario in listaUsuarios if usuario['CPF'] == cpfEscolhido)

    print("Informações completas do usuário requisitado:")
    print("Nome:", usuarioSelecionado['Nome'],
          "| CPF:", usuarioSelecionado['CPF'])
    print("Tipo:", usuarioSelecionado['Tipo'], "| Qnt. livros emprestados:",
          usuarioSelecionado['Qnt Livros emprestados'])
    if not usuarioSelecionado['Data p novo emprestimo']:
        print("Data p/ novo empréstimo(punição): nenhuma")
    else:
        print("Data p/ novo empréstimo:",
              usuarioSelecionado['Data p novo emprestimo'])
