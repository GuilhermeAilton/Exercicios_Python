n = int(input(""))

if n % 3 == 0 and n % 5 == 0 and n % 7 == 0 :
    print("O número {} não é divisível por 3,5 ou 7".formatn(n)) 

elif n % 3 != 0 and n % 5 != 0 and n % 7 != 0 :
    print("O número {} não é divisível por 3,5 ou 7 ".format(n))     
elif n % 3 == 0 and n % 5 == 0 and n % 7 != 0 :

    print("O número {} é divisível por 3 e 5 ".format(n)) 

elif n % 3 == 0 :
    print("O número {} é divisível por 3".format(n))
elif n % 5 == 0 :
    print("O número {} é divisível por 5".format(n))    
elif n % 7 == 0 :
    print("O número {} é divisível por 7 ".format(n))
elif n % 3 == 00 and n % 5 == 0 and n % 7 != 0 :
     print("O número {} é divisível por 3 e 5 ".format(n))     

