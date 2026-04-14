#Crie um programa que solicite 5 nomes e insira em uma lista

nomes = []
i = 0

while i < 5:
    nome = input("Digite o nome: ")
    nomes.append(nome)
    print(nomes)
    i += 1

#com for

for i in range(5):
    nome = input("Digite o nome: ")
    nomes.append(nome)
    print(nomes)