import os
import csv 
from .Auxiliares import*

def CadastrarNovoUsuario():
    os.system("clear")
    print(" - Cadastrar Usuario - ")
    print("")
    Usuario = {}
    print("O usuário é Professor(a) ou Aluno(a)?")
    resposta= input("-> ")
    if resposta.upper() == "Professor":
        Usuario.update({"Tipo": resposta})
    elif resposta.upper( == "Professora")
        Usuario.update({"Tipo": resposta})
    elif resposta.upper() == "Aluno":
        Usuario.update({"Tipo": resposta})
    elif resposta.upper() == "Aluna":
        Usuario.update({"Tipo": resposta})
    else:
        input('Resposta inválida. Pressione qualquer tecla...')
        CadastrarNovoUsuario()
    print("Digite seu CPF:")
    CPF = input("-> ")
    Usuario.update({"CPF": CPF})
    print("Digite seu nome:")
    Nome = input("-> ")
    Usuario.update({"Nome": Nome})
    Usuario.update({"QuantLivrosEmprestado": 0})
    Usuario.update({"Data": ""})
    arquivoExiste = os.path.isfile("livros.csv")

    with open("usuarios.csv", "a", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=camposUsuarios())
        if not arquivoExiste:
            escritor.writeheader()

        escritor.writerow(Usuario)
    arquivo.close()

def AtualizarUsuario():


def BuscarUsuario():
    