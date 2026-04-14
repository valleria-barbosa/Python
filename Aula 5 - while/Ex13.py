#Crie um programa que solicite 5 números inteiros, armazene em uma lista o seu valor ao quadrado.
lista = []
i = 0
while i <5:
    numero = int(input("Digite o número: "))
    quadrado = numero**2
    lista.append(quadrado)
    print(lista)
    i += 1