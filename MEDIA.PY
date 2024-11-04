import math

opcao = int(input("Digite a opção desejada (1 - Triângulo, 2 - Trapézio, 3 - Paralelogramo, 4 - Hexágono regular): "))

if opcao == 1:
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    area = (base * altura) / 2
    forma = "triângulo"
elif opcao == 2:
    base_maior = float(input("Digite a base maior do trapézio: "))
    base_menor = float(input("Digite a base menor do trapézio: "))
    altura = float(input("Digite a altura do trapézio: "))
    area = ((base_maior + base_menor) * altura) / 2
    forma = "trapézio"
elif opcao == 3:
    base = float(input("Digite a base do paralelogramo: "))
    altura = float(input("Digite a altura do paralelogramo: "))
    area = base * altura
    forma = "paralelogramo"
elif opcao == 4:
    lado = float(input("Digite o lado do hexágono regular: "))
    area = 3 * ((lado**2 * math.sqrt(3)) / 2)
    forma = "hexágono regular"
else:
    print("Forma geométrica não cadastrada")
    exit()

print("A área do", forma, "é igual a: {:.2f}".format(area))
