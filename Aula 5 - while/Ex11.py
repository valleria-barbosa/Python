#Cadastro de alunos:crie um algoritmo que solicite 3 nomes e 3 idades.Deixe a informação em uma lista no formato nome-idade
i = 0
lista = []
while i < 3:
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    nome_idade = [nome,idade]
    lista.append(nome_idade)
    print(lista)
    i += 1

#Outro modo de fazer uma lista dentro de lista
 #lista.append([nome,idade])