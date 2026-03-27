# Ex.17 - Crie um algoritmo para perguntar para o usuário qual o dia da semana, caso seja sábado, escreva "Dia de festa". Caso seja domingo, pergunte sobre a condição física do usuário, se estiver com dores de cabeça, printe "Recuperando, então, precisa descansar." Caso contrário, apenas descanse. Caso não seja sábado ou domingo, mostre "Trabalhando, trabalhando e trabalhando!

diaSemana = str(input("Digite o dia da semana: "))

if diaSemana == "domingo":
    dor = str(input("Esta com dor? (Responda sim ou nao): "))
    if dor == "sim" :
        print("Recuperando, então, precisa descansar.")
    else:
        print("Apenas descanse")
elif diaSemana == "sabado" or diaSemana == "sábado":
    print("Dia de festa")
else:
    print("Trabalhando, trabalhando, trabalhando.")