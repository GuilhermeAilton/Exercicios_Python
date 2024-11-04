a = int (input(""))
b = int (input(""))
c = int (input(""))

mult = False



for i in range (a,b+1) :
 if i % c == 0 :
        mult = True
        print(f'{i} eh multiplo de {c}')
if not mult :
   print(f'nao ha multiplos de {c} em [{a};{b}]')
      