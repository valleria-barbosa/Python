#Ex 6 - Crie um algoritmo usando while true para simular um menu interativo. Se a opção for 1 print olá, se opção for a 2, print sair

while True:
    opcao = int(input("Digite 1 - para olá, digite 2 - para sair"))
    if opcao ==  1:
        print("Olá")
    elif opcao == 2:
        print("Sair")
        break
