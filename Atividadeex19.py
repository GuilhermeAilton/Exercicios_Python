votos = []
percentual = []
w = 0
u= 0
l=0
n=0
m=0
o =0
total = 0
percentualu=percentualw=percentuall=percentualn=percentualm=percentualo= 0
Maisvotado = 0

while True :
    print("Qual o melhor Sistema Operacional para uso de servidores?")
    print("\n")
    print("Escolha um dos números para votar : \n")
    print(
          "1- Windows Server\n",
          "2- Unix\n",
          "3- Linux\n",
          "4- Netware\n",
          "5- Mac OS\n",
          "6- Outro\n"
          
          
          )
    
    voto = int (input("Digite um número para votar : "))
    votos.append(voto)
    if voto != False:
         total+= 1
    if voto == 0 :
         break     
    w = votos.count(1)
    u = votos.count(2)
    l= votos.count(3)
    n = votos.count(4)
    m = votos.count(5)
    o = votos.count(6)
    


    percentualw = (w*100)/total
    percentualu = (u*100)/total
    percentuall = (l*100)/total
    percentualn = (n*100)/total
    percentualm = (m*100)/total
    percentualo = (o*100)/total           
     
    round(percentualw)
    round(percentualu)
    round(percentuall)
    round(percentualn)
    round(percentualm)
    round(percentualo)

    
print(f"""
               
               
Sistema Operacional       Votos      %
---------------------     -----     ---
 Windows Server            {w}        {(percentualw)}%
 Unix                      {u}        {(percentualu)}%
 Linux                     {l}        {(percentuall)}%           
 Netware                   {n}        {(percentualn)}%
 Mac Os                    {m}        {(percentualm)}%
 Outro                     {o}        {(percentualo)}%
---------------------     ----- 
 Total                     {total}
                                            
               """.format(total,percentuall,percentualw,percentualn,percentualu,percentualo,percentualm,w,u,l,n,m,o))

      

