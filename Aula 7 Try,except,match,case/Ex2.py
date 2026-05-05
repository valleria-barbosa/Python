#Crie uma estrutura com try/except a qual calcule e traga um erro para calcular a area de um ratangulo e circulo com estrutura de input para o usuário. Além disso, o usuário deve escolher a figura geométrica.



try:
    figura = int(input("Digite qual figura quer. 1 - circulo, 2 - retangulo"))
    if figura == 1:
        raio = float(input("Digite o raio: "))
        area = 3.1415*raio**2
        print(area)
    elif figura == 2:
        base = float(input("Digite a base: "))
        altura = float(input("Digite a altura: "))
        area = base * altura
        print(area)
except ValueError:
    print("Valor não númerico!")