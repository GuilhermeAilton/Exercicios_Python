'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem; '''


lista =[]
cont = 0
soma= 0
media =0
acmed= []
abaixo7 = []
while True:
    n = float(input("Digite suas notas : "))
    if n == -1 :
        break

    lista.append(n)
    cont += 1
    soma = soma + n

media = soma/cont

for i in lista :
    if i > media :
        acmed.append(i)
    if i < 7  :
        abaixo7.append(i)




print(lista, end=" ")
lista.reverse()
print(" ")
print(lista, end=" \n ")
print(soma)
print(media)
print(acmed)
print(abaixo7)


print(" SESSÃO ENCERRADA COM SUCESSO ")

