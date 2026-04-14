num = int(input("Insia um número: "))

fat = 1
i = 1

while i <= num:
    fat *= i
    i += 1
    print(f"O valor é: {fat}")

#cria um fatorial de um número,
# se colocar por acaso 5 será 5x4x3x2x1. Ou seja 5!