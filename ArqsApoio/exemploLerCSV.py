import csv


f = open("dadosExemplo.csv", newline='')
pessoas = csv.reader(f, delimiter=";")
for linha in pessoas:
	print(linha[0], "\t", linha[1], "\t", linha[2])

# abrindo e usando como um dictionary
print("\n\nExibindo usando como dictionary\n\n")
f.close()
f = open("dadosExemplo.csv", newline='')
pessoas = csv.DictReader(f, delimiter=";")
for linha in pessoas:
	print(linha['Id'], "\t", linha['Nome'], "\t", linha['Idade'])
