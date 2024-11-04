
cont1 = cont2 = cont3 = cont4 = 0
while True :
    n = int (input (" Digite um número : ")) 

    if n > 0 and n <= 25 :
        cont1 = cont1 + 1
    elif n >= 26 and n <= 50 :
        cont2 = cont2 + 1
    elif n >= 51 and n <=75 :
         cont3 = cont3 + 1
    elif n >= 76 and n <= 100 :
         cont4 = cont4 + 1
          
    elif n < 0 :
        print("0-25: ",cont1)
        print("26-50: ",cont2)
        print("51-75: ",cont3)
        print("76-100: ",cont4)
        

