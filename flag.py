cont = 0
soma = 0

while True :
  n = int (input('Digite um valor ou 999 para parar : '))
  if n < 999 : 
    soma = soma + n
    cont = cont + 1
  elif n == 999 : 
    print('A soma dos',cont,'valores foi',soma )
    break
    


  
    
