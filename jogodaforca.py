
palavra = 'Guilherme'
letras = []
chances =7
ganhou = False

while True :
    for letra in palavra :
        if letra in letras:
            print(letra, end=" ")
        else:
            print("_",end=" ")              


    print("")
    tentativa  = input("Escolha uma letra para para advinhar : ").lower()
    letras.append(tentativa)

    if tentativa.lower()  not in palavra.lower() :
     chances -= 1
    if chances == 0 :
     print("Você perdeu")  



if ganhou:
    print(f"Parabéns voce ganhou")
else :
    print(f"Você perdeu")