#EX.8 Crie um algoritmo para solicitar nome, porém, mande apenas os nomes com caracteres >=3 para a lista de nomes
lista = []
while True:
    nome = input("Digite o nome: ")
    if len(nome) >=3:
        lista.append(nome)
        print(lista)