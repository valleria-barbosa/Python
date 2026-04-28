#Ex.11 Filtrar palavras com letra proibida. Se aparecer palavra com x, não mostrar palavra na lista

lista = []
while True:
    nome = input("Digite o nome: ")
    if "x" in nome:
        continue
    else:
        lista.append(nome)
        print(lista)