
lista = []
for i in range (1,6):
    n= int (input('Digite o {}º valor : '.format(i))) 
    lista.append(n)
   

for i in range(len(lista)):
    print(f"Posição {i + 1}: {lista[i]}")

lista.reverse()
print(lista)