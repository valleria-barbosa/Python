# Ex.18 - Crie um algoritmo para solicitar a escolha do menu do café da manhã. Opções: ovos, panquecas, wafles e frutas.
# Acompanhamentos: bacon, queijo, pão, presunto, manteiga e limão. Tipos de frutas: abacaxi, maçã, banana e uvas.

escolha = input("Escolha a opção para o café da manhã: ovo, panqueca, wafles e frutas: ")

if escolha == "ovo":
    acompanhamento = input("Escolha seu acompanhamento: bacon, queijo, pão, presunto: ")
    if acompanhamento == "bacon":
        print("Sua opção é ovo com bacon.")
    elif acompanhamento == "queijo":
        print("Sua opção é ovo com queijo.")
    elif acompanhamento == "pao":
        print("Sua escolha é pão com ovo.")
    elif acompanhamento == "presunto":
        print("Sua escolha é ovo com presunto.")
    else:
        print("Você prefere sem acompanhamento.")
elif escolha == "panqueca":
    print("Você quer panqueca.")
elif escolha == "wafles":
    print("Você escolheu wafles.")
elif escolha == "frutas":
    qfruta = input("Qual fruta você quer? Temos abacaxi, maçã, banana e uva: ")
    if qfruta == "abacaxi":
        print("Você quer abacaxi.")
    elif qfruta == "maca":
        print("Você escolheu maçã.")
    elif qfruta == "banana":
        print("Você escolheu banana.")
    else:
        print("Você escolheu uva")
else:
    print("Você não quer café da manhã")