#EX.9 Crie um algoritmo com listas de notas válidas. Se -1, pare a estrutura, se nota < 0 ou nota > 10, continue. Ao final, calcule a média das notas.

lista = []

while True:
    nota = int(input("Digite a nota: "))
    if nota == -1:
        break
    elif nota > 10:
        print("Nota inválida, digite uma nota de 0 a 10")
    else:
        lista.append(nota)
        print(lista)

soma = 0
for i in lista:
    soma += i

total = soma / len(lista)
print(total)