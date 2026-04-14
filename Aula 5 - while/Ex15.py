#Crie um programa que solicite números para o usuário, pare quando digitar 0, armazene os números em uma lista. Mostre a lista completa e a soma dos valores.

lista = []
soma = 0
while True:
    numero = int(input("Digite o número: "))
    if numero == 0:
        break
    lista.append(numero)
    soma += numero
    print(lista)
    print(f"A soma é: {soma}")