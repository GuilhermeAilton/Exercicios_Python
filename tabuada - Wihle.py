cont = 1
while True :

 print('Menu de  opções :')
 print('\n 1 - Adição\n 2- Multiplicção\n 3- Subtração\n 4 - Divisâo -\n 0 SAIR \n ')

 valor=int(input("Digite o número para calcular sua tabuada : "))
 if valor == 5 :
  break
 elif valor >= 1 and valor < 5:
    num = int (input('Tabuada de : '))
  
    while cont <= 10 :    
     if valor == 1:
        soma = num + cont
        print('%d + %d  = %d' % (num,cont,soma))
        cont = cont + 1
     if valor==2 :
          mu = num * cont
          print('%d * %d  = %d' % (num,cont,mu))
          cont = cont + 1
     if valor==3 :
       sub = num - cont
       cont = cont + 1
       print('%d - %d  = %d' % (num,cont,sub))    
     elif valor==4 :
       div = num/cont
       cont = cont + 1 
       print('%d : %d  = %f' % (num,cont,div))




      
