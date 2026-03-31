nome = input("Digite o nome do cliente: ")
valor = float(input("Digite o valor da compra: "))
tipo = input("Digite o tipo de cliente (comum/premium): ").lower()

if tipo =="comum":
    if valor >= 200 :
        desconto = valor * 0.10
    else:
        desconto = valor *0.05
elif tipo == "premium":
    if valor >= 200:
        desconto = valor * 0.20
    else:
        desconto = valor * 0.10
else: 
    desconto = 0
    print("Você não receberá nenhum desconto")

if valor != 0:
    valor_final = valor - desconto
    print("Cliente: ", nome)
    print("Valor da compra: ", valor)
    print ("Desconto: ", desconto)
    print("Valor final:", valor final) 