consoantes = []



for cont in  range (11) :
    letras= str(input("Digite uma letra : ")).lower()

    if letras !="a" and letras != "e" and letras != "i" and letras !="o" and letras !="u":
        consoantes.append(letras) 

print(consoantes)

