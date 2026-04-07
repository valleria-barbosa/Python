#EX5 Soma e média de valores digitados pelo usuário. Crie um algoritmo para solicitar 5 valores não inteiros, insira em uma lista. Após isso, crie uma estrutura para somar e retornar a média dos elementos desta lista.

lista_valores = []
soma = 0
for i in range (1,6):
    numero = float(input("Digite o valor: "))
    lista_valores.append(numero)
    soma += numero

media = soma/len(lista_valores)
print(f"A soma é {soma} e a média é {media}")