cont = 0

while True :
    n = int (input(""))
    if n == 0:
        break

    for i in range (1,n+1) :
        if n % i == 0 or n == 1 :
          cont += 1  
        else:
            pass
if cont == 2 :
    print('Número primo digitado')        
else:
    print('Número primo não digitado')    