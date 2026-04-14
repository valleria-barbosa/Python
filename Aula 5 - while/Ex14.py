#Crie um programa que solicite nome, curso e idade de 3 pessoas, armazene cada pessoa como uma lista dentro de uma lista_completa.
lista_completa = []
i = 0
while i < 3:
    nome = input("Digite o nome: ")
    curso = input("Digite o curso: ")
    idade = int(input("Digite a idade: "))
    nome_curso_idade = [nome, curso, idade]
    lista_completa.append(nome_curso_idade)
    print(lista_completa)
    i += 1