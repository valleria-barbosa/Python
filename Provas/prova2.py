n1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (adicao, subtracao, divisao. multiplicacao: )").lower()
n2 = float(input("Digite o segundo número: "))

if operacao == "adicao":
    soma = n1 + n2
    print(soma)
elif operacao == "subtracao":
    subtracao = n1 - n2
    print(subtracao)
elif operacao == "divisao":
    if n2 == 0:
        print("Não é possível dividir por zero.")
    else:
        divisao = n1 / n2
        print(divisao)
elif operacao == "multiplicacao":
    multiplicacao = n1 * n2
    print(multiplicacao)
else:
    print("Operação inválida")
