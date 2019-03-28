import csv

# Gravando o mesmo arquivo usando dictionary
f = open("dadosExemplo2.csv", "a")
campos = ["Id", "Nome", "Idade"]
pessoas = csv.DictWriter(f, fieldnames=campos)
ident = int(input("Entre com um id: ")) 
nome = input("Entre com um nome: ")
idade = int(input("Entre com uma idade: "))
# escreve o cabeçalho do arquivo, com os campos que serão
# usados pelo DictReader
pessoas.writeheader();
info = dict(Id=ident, Nome=nome, Idade=idade)
pessoas.writerow( info )
# gravando dados no arquivo
f.flush()
f.close()

f = open("dadosExemplo2.csv", "a")
# pessoas = csv.reader(f, delimiter=";")
# gravando uma nova informação
pessoas = csv.writer(f, delimiter=';')
ident = int(input("Entre com um id: ")) 
nome = input("Entre com um nome: ")
idade = int(input("Entre com uma idade: "))
pessoas.writerow( [ ident, nome, idade] )
# gravando dados no arquivo
f.flush()
f.close()
