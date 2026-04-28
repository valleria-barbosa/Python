#Ex.12 Criar um programa a qual ao selecionar opção 1, solicitar e enviar nomes para uma lista nomes, opção 2, solicitar e enviar cpfs para uma lista cpf e ao digitar 3, solicitar e enviar idade para a lista_idade. Crie também uma estrutura para juntar todas as listas

nomes = []
cpfs = []
idades = []

while True:
    opcao = int(input("Digite 1 para nome, 2 para cpf e 3 para idade, 4 sair"))
    if opcao == 1:
        nome = input("Digite o nome: ")
        nomes.append(nome)
        print(nomes)
    elif opcao == 2:
        cpf = int(input("Digite o cpf: "))
        cpfs.append(cpf)
        print(cpfs)
    elif opcao == 3:
        idade = int(input("Digite a idade: "))
        idades.append(idade)
        print(idades)
    else:
        break

juntar = nomes + cpfs + idades
print(juntar)