# Ex.15 - Solicite número e verifique se é maior do que zero, se for, crie uma estrutura de condição aninhada para verificar se este número é par, se for, printe positivo e par. Se não for, positivo e ímpar. Se número for igual a zero, printe zero.  Caso contrário, negativo.

numero = int(input("Digite o número: "))

if numero > 0:
    if numero % 2 == 0:
        print("Numero é positivo e par.")
    else:
        print("Número positivo ímpar.")
elif numero == 0:
    print("Número Zero")
else:
    print("Número negativo.")
