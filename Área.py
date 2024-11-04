
op = int (input("Digite uma opção "))
if op == 1:
 base = float (input(""))
 al = float (input(""))
 A = ( base * al ) / 2
 print(f"A area da forma do triângulo é igual a: {A:.2f}")
 

if op == 2 :
  Bm = float (input("Base Maior: "))
  b = float (input("Base Menor: "))
  al = float(input("Altura: "))
  A = ((Bm + b )*al)/2
  print(f"A area da forma do trapézio é igual a: {A:.2f}")

if op == 3 :
    base = float (input(""))
    al = float (input(""))
    A = b * al
    print(f"A area da forma do paralelogramo é igual a: {A:.2f}")
if op == 4 :
   l = float(input("Digite o lado: "))
   A = 3 * ((l**2 * 3** (1/2)) /2 ) 
   print(f"A area da forma do hexágano regular é igual a: {A:.2f}")
 
elif op < 1 or op >= 5 :
   print("Forma geométrica não cadastrada")



  
     


