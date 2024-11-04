
idade= []
menor = []
soma = 0
media = 0
for i in range(10,31):
 print(i, end=" ")
 
 idade.append(i)


soma = sum (idade)
media= soma/30
print(media)
for i in idade :
 if i< media :
  menor.append(i)



print(menor)