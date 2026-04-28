#Ex.1 - lista de números

numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    print(numeros)

#Ex.2 lista de números e nomes

numeros = []
nomes = []

for i in range(5):
    numero = int(input("Digite um número: "))
    nome = input("Digite um nome: ")

    numeros.append(numero)
    nomes.append(nome)
    print(numeros)
    print(nomes)

#EX.3 estrutura com break e continue
lista_universidades = ['USP', 'FIAP', 'UNICAMP', 'UNESP', 'MIT']

for k in lista_universidades:
    if k == 'MIT':
        break                 #independente da quantidade de coisas que tem, o código para no break
    print(f"Universidade - {k}")

#EX.4 Estrutura com continue

lista_universidades = ['USP', 'FIAP', 'UNICAMP', 'UNESP', 'MIT']

for k in lista_universidades:
    if k == "UNESP":
        continue              #o continue não mostra a palavra da condição, mas continua a mostrar os seguintes.
    
    print(k)