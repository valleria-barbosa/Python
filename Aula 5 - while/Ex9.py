#Crie um programa para gerar uma tabuada, a partir de duas váriaveis (numero e limite)

i = 0
numero = int(input("Digite o número: "))

while i <= 10:
    limite = numero * i
    print(f"{numero} * {i} = {limite}")
    i += 1
