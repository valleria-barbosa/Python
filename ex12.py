# Ex.12 - Solicite usuário e senha. Se usuário for igual a admin, crie uma estrutura de condição aninhada para solicitar senha e se a mesma for "1234", mostre que o usuário terá acesso total. Caso o usuário insira a senha incorreta, mostre senha incorreta. Caso usuário insira usuário incorreto, mostre "usuário incorreto".

usuario = input("Digite o nome do usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin":
    if senha == "1234":
        print("Acesso total concedido.")
    else:
        print("Senha incorreta.")
else:
    if senha == "1234":
        print("Usuário incorreto.")
    else:
         print("Usuário incorreto e senha incorreta.")