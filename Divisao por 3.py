
while True :

  n = int (input("Digite um número para saber se é divisível por 3 : "))
  if n > 9999 :
    break
  if n < 1000 :
     a= n // 1 % 10
     b = n // 10 % 10
     c = n // 100 % 10
     res = (c + a + b) % 3

  if res == 0 :
        print("Numero divisel por 3 ")

  else:
    print("Número não divivel por 3")
  

  if n >= 1000 :
     a= n // 1 % 10
     b = n // 10 % 10
     c = n // 100 % 10
     d = n // 1000 % 10
     res = (c + a + b + d) % 3     
     if res == 0 :
        print("Numero divisel por 3 ")

     else:
      print("Número não divivel por 3")
  




