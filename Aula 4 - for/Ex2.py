#EX6 Crie uma estrutura para solicitar 10 números para o usuário. Após isso crie duas listas (par e ímpar) e insira os valores pares na lista par, valores ímpares na lista ímpar. Print a lista completa, lista par e lista ímpar.

lista = []
par = []
impar = []

for i in range(1,11):
    numero = int(input("Digite o número: "))
    if numero %2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
    lista.append(numero)
print("Lista com todos os valores ", lista)
print("Lista com números pares" ,par)
print("Lista com números ímpares" ,impar)