

gui = [5.4,10,15,12]
ailton = [9.7,8.3,4.3,20]
maiornota = 0
maiornota1 = 0
maiornota2 = 0
maiornota3 = 0
soma = 0
soma2 = 0
gui.sort(reverse=True)
ailton.sort(reverse=True)


for nota in gui :
    if nota > maiornota:
        maiornota = nota
    if nota > maiornota1 and nota < maiornota:
        maiornota1 = nota
soma = maiornota + maiornota1 
     
for nota in ailton :
    if nota > maiornota2:
        maiornota2 = nota
    if nota > maiornota3 and nota < maiornota2:
        maiornota3 = nota
soma2 = maiornota2 + maiornota3

if soma > soma2:
 print("GUILHERME CAMPEÃO")

else:
    print("AILTON CAMPEÃO")