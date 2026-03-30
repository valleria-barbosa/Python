#Escreva um programa que indentifique quais valores são ímpares em uma range de 1 a 51 e calcule a média destes valores.
soma = 0
contador = 0
for i in range (1,51):
    if i%2 !=0:
        soma += i
        contador += 1
media = soma/contador
print("A média é: ", media)
