while True:
    A = int(input("Digite o valor de A  "))
    B = int(input("Digite o valor de B: "))

    if A > 0 and B < 100 and B > A:
        break
    else:
        print("")
for num in range(A, B + 1):
    if num % 2 != 0:
        print(num)
