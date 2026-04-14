#Crie um programa que solicite 5 números inteiros e decremente os valores inseridos pelo usuário.
i = 0
decremento = 0
while i < 5:
    num = int(input("Digite o número: "))
    decremento -= num
    print(decremento)
    i += 1