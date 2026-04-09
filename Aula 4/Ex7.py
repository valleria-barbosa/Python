#EX11 Crie um algoritmo para simular sistema com menu. O usuário pode cadastrar, listar ou sair da estrutura.
#Se opção 1, solicite nome, idade, cidade e deixe estas informações em uma estrutura de lista dentro de lista.
#Se opção 2, print o respectivo nome, idade e cidade da pessoa.
#e opção 3, crie uma estrutura para sair do código.

pessoa = []
while True:
    opcao = int(input("Qual opção deseja? 1-cadastrar, 2-listar ou 3-sair: "))
    if opcao == 1:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        cidade = input("Digite a cidade: ")

        nome_idade_cidade = [nome,idade,cidade]
        pessoa.append(nome_idade_cidade)

        print("Cadastro realizado com sucesso!")

    elif opcao == 2:
        if len(pessoa) == 0:
            print("Não existe cadastro")
        else:
            for i in pessoa:
                print(f"Nome: {i[0]} Idade: {i[1]} Cidade:{i[2]}")
    elif opcao == 3:
        print("Saindo do sistema")
        break
    else:
        print("Opção inválida.")