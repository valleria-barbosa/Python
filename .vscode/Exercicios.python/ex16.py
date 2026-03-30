# Ex.16 - Solicite valor e se a pessoa é vip ou não. Se valor maior ou igual a 200, crie estrutura de condição aninhada para verificar se a pessoa é vip, se for, ofereça 20% de desconto sobre o valor e mostre o valor a ser descontado e o valor final considerando o desconto. Se não for vip, ofereça o desconto de 10%.

valor = float(input("Digite o valor: "))
vip = str(input("Você é VIP? (responda com sim ou nao:)"))

if valor >= 200:
    if vip == "sim":
        desconto = valor * 0.2
        valor_final = valor - desconto
        print(f"Você recebeu o desconto de 20%. O valor do desconto é {desconto}. No total ficou {valor_final}")
    else:
        desconto = valor * 0.1
        valor_final = valor - desconto
        print(f"Você recebeu o desconto de 10%. O valor do desconto é {desconto}. No total ficou {valor_final}")
else:
    print(f"Você não recebeu desconto, o valor total é {valor}")