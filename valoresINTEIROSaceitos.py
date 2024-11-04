cont =  1
soma = 0

A = int (input("Digite o valor A : " ))
B = int (input("Digite o valor B : " ))
C = int (input("Digite o valor C : " ))
D = int (input("Digite o valor D : " )) 
if B > C :
     soma = soma + 1   
if D > A  :  
     soma = soma + 1
if C + D > A + B :
      soma = soma + 1
if A and B > 0 :
     soma = soma + 1
if A % 2 == 0 :
       soma = soma + 1

if soma == 5 :
     print("Valores aceitos")
if soma >= 3  and soma < 5  :
     print("Valores quase aceitos")
if soma >= 1 and soma <= 2  :
     print("Valores quase rejeitados")
if soma == 0 :
     print("Valores rejeitados")          
             

print (soma