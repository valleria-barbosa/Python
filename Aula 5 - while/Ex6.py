#Encontrando a soma dos números em uma lista usando while
lista = [23,45,12,10,25]

soma = 0
i = 0

while i < len(lista):
    soma += lista[i]
    i += 1
    print(soma)
