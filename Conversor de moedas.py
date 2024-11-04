moedas = ['Dolar','Euro','Libra']
print("SEJA BEM-VINDO AO CONVERSOR DE MOEDAS\n")

while True :
    tm = len(moedas)
    cont = 0
    
    convesor = float(input("\nDigite o valor em R$ para ser convertido : "))

    if convesor ==0 :
        break

    for moeda in moedas:
         cont += 1
         print(f'{cont} - {moeda}')
    op = int(input('Escolha o formato da moeda para ser covertido : '))
    if op == 1 :
        resul = convesor * 0.21
        print(f"\nO valor convertido em Dolar : {resul:.2f} ")
    elif op == 2 :
        resul =convesor * 0.19
        print(f"\nO valor convertido em Dolar: {resul:.2f} ")
    if op == 3 :
        resul = convesor * 0.19      
        print(f"\nO valor convertido em Dolar : {resul:.2f} ")
