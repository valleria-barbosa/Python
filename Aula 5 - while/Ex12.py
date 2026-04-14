#Crie uma estrutura que solicite itens de compra de forma que só seja possível sair da estrutura de repetição, caso o usuário digite sair. Coloque os itens em uma lista.
lista = []
while True:
    item = input("Digite o item: ")
    if item == "sair":
        break
    lista.append(item)
    print(lista)