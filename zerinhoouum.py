import random

while True:
 eu = int( input ("Digite zero ou um "))
 computador = random.randint(0,1)
 computador2 = random.randint(0,1)
 if eu > 1 :
   print("Digte um número correto") 
 elif eu == computador == computador2 :
    print("Deu empate")
    print(eu, computador, computador2)
 elif eu != computador and eu != computador2:
    print("VC GANHOU")    
    print(eu, computador, computador2)
 elif computador2 != computador and eu != computador2:
   print(" PC 2 GANHOU")   