#EX10 Crie um algoritmo para solicitar nome e nota para 4 alunos. Insira em uma estrutura com listas dentro de lista(nome,nota). Após isso, crie uma estrutura para mostrar os alunos aprovados com nota maior ou igual a 6, mostrando o respectivo nome e nota. Crie também uma estrutura para mostrar os alunos com nota menor do que 6 e mostre o respectivo nome e nota.

lista_aprovados = []
lista_reprovados = []
for i in range(4):
    nome = input("Digite o nome: ")
    nota = float(input("Digite a nota: "))
    nome_nota = [nome,nota]
    if nota >= 6:
        lista_aprovados.append(nome_nota)
    else:
        lista_reprovados.append(nome_nota)

print(f"A lista de aprovados é: {lista_aprovados}")
print(f"A lista de reprovados é: {lista_reprovados}")
