#EX8 Vamos fazer um algoritmo para cadastro com média. Solicite 3 informações: nome, nota1 e nota2 três vezes. Após isso, calcule a média de cada aluno e retorne uma lista contendo nome, nota1,nota2, média de cada aluno.
#Estrutura: lista = [[nome,nota1,nota2], [nome, nota1 ,nota2],...,]

k=0
media = 0
lista = []
for i in range(3):
    nome = input("Digite o nome: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    media = (nota1+nota2)/2
    nota_media = [nome,nota1,nota2,media]
    lista.append(nota_media)

print(lista)