import math

lista = [ "DIVISÃO", 'SOMA','POTÊNCIAÇÃO', 'RAIZ QUADRADA','SUBTRAÇÃO','TABUADA']
x = 0
resul = 0
print("Menu de opções : ")
for i in lista :
   
    x = x + 1
    print(x,'-',i)

op =int (input("SELECIONE UMA OPÇÃO : "))
num1 = int(input("Digite um valor : "))
num2 = int ( input("Digite outro valor : "))

if op == 1:
 resul = num1 / num2
 print( resul)
if op == 2:
 resul = num1 + num2 
 print(resul)
if op ==3 :
  resul =num1**num2
  print(resul) 
if op == 4 :
  resul = math.sqrt(num1)
  print( int (resul)) 
if op == 5 :
  resul = num1 - num2 
  print(resul)  

if op == 6 :
  for i in range(1,11) :
    resul = num1 * i 
    print(f"{num1} x {i} : {resul}")

if op == 7 :
  a = 0
      