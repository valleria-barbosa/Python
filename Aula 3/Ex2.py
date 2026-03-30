#Crie um programa que imprima quais são os números pares de 1 a 50 e calcule a soma dos valores pares.
soma = 0
for i in range (1,51):
    if i%2 == 0:
        print(i)
        soma += i
print("A soma dos números pares de 1 a 50 é: " , soma)
    