#Crie uma estrutura com try/except para converter temperatura celsius em fahreinht.

try:
    celsius = float(input("Digite o grau em Celsius: "))
    fahreinht = (celsius * 9/5) + 32
    print(fahreinht)
except ValueError:
    print("Digite um número válido")