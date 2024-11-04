def calcular_resto(dividendo, divisor):
    while dividendo >= divisor:
        dividendo -= divisor

    return dividendo

# Solicitar números ao usuário
dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

resto = calcular_resto(dividendo, divisor)
print("O resto da divisão entre", dividendo, "e", divisor, "é:", resto)


    