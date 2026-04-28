#EX.10 Vamos criar um sistema de menu simples.
#1 - adicionar número 
#2 - remover último número // lista.pop() remove o último item da lista. lista.pop(0) remove o primeiro item da lista
#3 - mostrar lista
#4 - sair

lista = []

while True:

    opcao = int(input("Digite 1 - adicionar número / 2 - remover último número / 3 - mostrar lista / 4 - sair "))

    if opcao == 1:
        numero = input("Digite um número: ")
        lista.append(numero)
        print(lista)

    elif opcao == 2:
        lista.pop()
        print(lista)

    elif opcao == 3:
        print(lista)
        
    else:
        break