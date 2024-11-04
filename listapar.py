'''Inicialize uma lista de 20 números inteiros. Armazene
os números pares em uma lista PAR e os números
ímpares em uma lista IMPAR. Imprima as listas PAR
e IMPAR'''


lista = []
listapar= []
listaimpar= []
for n in range (1,21) :
    lista.append(n)
    if n % 2 == 0 :
        listapar.append(n)
    else:
        listaimpar.append(n)

print(lista)
print(listapar)
print(listaimpar)
    