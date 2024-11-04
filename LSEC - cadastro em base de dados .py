identidade = []
nom = []
ida = []
p = []
alt = []
cont = 0
tm = int (input(''))

while cont < tm :
    rg = int(input())
    identidade.append(rg)
    nome = str(input())
    nom.append(nome)
    idade= int(input())
    ida.append(idade)
    peso = int(input())
    p.append(peso)  
    altura = float(input())
    alt.append(altura)
    cont +=1

for i in range (tm):
    print(identidade[i],nom[i],ida[i],p[i],alt[i])