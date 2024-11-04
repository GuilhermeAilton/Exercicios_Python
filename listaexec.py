lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(lista[1:10])
print(lista[8:14])
for i in lista :
   if i % 2 == 0 :
      print(i) 

for i in lista :
   if i % 2 != 0 :
      print(i)

print("")      
for i in lista :
   if i % 2 == 0 or i % 3 == 0 or i % 4 == 0 :
      print(i)  


#lista reversa
rev = list(reversed(lista))
print(rev) 
soma1 = 0
soma2 = 0
for i in lista[10:16] :
   soma1 = soma1 + i
for i in lista [3:10]:
   soma2= soma2 + i 


total= soma1/soma2      
print(f"O resultado da razão : ",total)