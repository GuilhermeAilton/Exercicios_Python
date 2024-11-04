alien_0 = {'cor':'verde', 'pontos' : 5}


alien_0['cor']= 'azul'
print(alien_0['cor'])
print(alien_0['pontos'])


alien_0['pontos'] = 4
print(alien_0['pontos'])

#Adicionando um atributo
alien_0['posicao_x'] = 10
alien_0['posicao_y'] = 10



for i in alien_0 :
    print(i)
#deletando um atributo 
del alien_0['posicao_x']    




#Pecorrer um dicionario com metodo items

for atr , val in alien_0.items():
    print(atr,val)
 