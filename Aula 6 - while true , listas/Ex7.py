#Ex.7 Crie um algoritmo usando while true para ignorar valores negativos. Se o número for 0, quebre a estrutura de repetição, caso contrário, envie cada número para uma lista

lista = []

while True:
    numero = int(input("Digite o número: "))
    if numero == 0:
        break
    elif numero < 0:
        print("Número negativo")
        continue
    else:
        lista.append(numero)
        print(lista)