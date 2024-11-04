
# # CRIANDO COPIA DE LISTAS INDEPENDENTE

# # números=[0,0,0,0,0] 
# # V=números[:]
# # V[0]=10
# # print (V)

# #FATIAMENTO DE LISTAS 

# L = [89,88,87,86,85]

# print(L[0:3])

# #Tamanho da lista

# L=[1,2,3]
# x=0
# print(len(L))
# while x < len(L):
#  print(L[x])
# #  x = x + 1


# Leitura das duas listas
# lista1 = input("Digite os elementos da primeira lista separados por espaço: ")
# lista2 = input("Digite os elementos da segunda lista separados por espaço: ")

# # Geração da terceira lista
# terceira_lista = lista1 + lista2

# # Imprimir a terceira lista
# print("Terceira lista gerada:", terceira_lista)
# último = 10
# fila = list(range(1,último+1))
# while True:
#  print("\nExistem %d clientes na fila" % len(fila))
#  print("Fila atual:", fila)
#  print("Digite F para adicionar um cliente ao fim da fila,")
#  print("ou A para realizar o atendimento. S para sair.")
#  operação = input("Operação (F, A ou S):")
#  if operação == "A":
#   if(len(fila))>0:
#     atendido = fila.pop(0)
#     print("Cliente %d atendido" % atendido)
#   else:
#     print("Fila vazia! Ninguém para atender.") 
#  elif operação == "F":
#   último+=1 # Incrementa o ticket do novo cliente
#   fila.append(último)
#  elif operação == "S":
#   break
#  else:
#   print("Operação inválida! Digite apenas F, A ou S!")




# pECORRER UMA LISTA


n = int (input('FATORIAL'))

for i in range (1,n):
   resul = n * i

print(resul)    