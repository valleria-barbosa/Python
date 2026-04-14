#Inserir estrutura de consição dentro do while

realizado = False

while not realizado:
    entrada = int(input("Insira alguma coisa: "))

    if entrada == 999:
        realizado = True
    else:
        print(entrada)

#Enquanto realizado for igual a false -> while not realizado.
#  while só será parado se colocar o 999.