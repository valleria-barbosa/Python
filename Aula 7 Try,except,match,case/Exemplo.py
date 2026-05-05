#Exemplo de dicionário

import pandas as pd

dados = {
    'produto': ['notebook', 'mouse', 'teclado', 'monitor', 'webcam'],
    'vendas': [1200,300,450,800,None],
    'lucro': [300,50,80,200,40],
    'ano': ['2022', '2022','2022', 'dois mil e vinte e dois']
}

print(dados)

dataFrame = pd.DataFrame(dados) #mostra em tabela
for coluna in ['vendas', 'lucro']:
    try:
        media = dataFrame[coluna].mean()
        print(f"Média da coluna {coluna} é {media}.")
    except KeyError:
        print(f"A coluna {coluna} não existe.")

#calculo média
media = dataFrame['lucro'].mean()

print(media)

#try/except
try:
    media = dataFrame['lucro'].mean()
    print(f"A média de lucro é {media}")
except KeyError:
    print("Essa coluna não existe.")

###############################################

try:
    dataFrame['relacao_vendas_lucro'] = dataFrame['lucro']/dataFrame['vendas']
except ZeroDivisionError:
    print("Não é possível dividir por zero!")
else:
    print("Margem calculada com sucesso")

##################################################
try:
    numero = int(input("Insira um número: "))
except ValueError:
    print("Valor não númerico. ")

#############################################
try:
    a = int(input("Insira um número: "))
    b = int(input("Insira um número: "))

    soma = a + b
    sub = a - b
    div = a / b
    print(soma)
    print(sub)
    print(div)

except ValueError:
    print("Valor não númerico. ")

except ZeroDivisionError:
    print("Erro: divisão por zero!")

##############################################
def entrada_numero():
    try:
        numero = int(input("Insira um número: "))
        print(numero)
    except ValueError:
        print("Valor não númerico.")
##############################################