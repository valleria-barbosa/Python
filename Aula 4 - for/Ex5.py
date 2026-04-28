#EX9 Crie um algoritmo para simular um sistema de compras, onde deverá ser solicitado nome 100x. Após isso, crie uma estrutura para quebrar a solicitação de nomes. Após isso, crie uma estrutura para solicitar preço, com isso, deixe o respectivo nome e preço juntos. Finalmente, mostre o valor total dos produtos.

lista_nome_preco = []
for i in range(100):
    nome = input("Digite o nome do produto: Se quer parar digite 'S' ")
    if nome == "S":
        break
    preco = float(input("Digite o valor:"))
    nome_preco = [nome,preco]
    lista_nome_preco.append(nome_preco)
    soma =+ preco
print(soma)
   
