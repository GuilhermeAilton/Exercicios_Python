listanome = []
listaidade = []
listacurso = []

while True:
    print('')
    print("Menu de Opções: [1-5]\n")
    print("1 - Cadastrar")
    print("2 - Remover")
    print("3 - Localizar Aluno")
    print("4 - Mostrar todos Alunos Cadastrados")
    print("5 - Sair\n")

    op = int(input('Selecione uma opção: '))
    
    if op > 5 or op < 1:
        print("\nSelecione uma opção válida")
    
    if op == 5:
        print("Guilherme Sistemas Agradece!!!!")
        break
    
    if op == 1:
        nome = input("\nDigite seu nome completo: ").upper().strip()
        listanome.append(nome)
        idade = int(input("\nDigite sua idade: "))
        listaidade.append(idade)
        curso = str(input('\nDigite seu curso: ')).upper().strip()
        listacurso.append(curso)
        print("\nALUNO CADASTRADO COM SUCESSO ")
    
    if op == 2:
        print(listanome, listaidade, listacurso, "\n")
        print("\n")
        nome = input("Digite o nome do aluno para ser excluído do sistema: ").upper().strip()
        if nome in listanome:
            indice = listanome.index(nome)
            del listanome[indice]
            del listaidade[indice]
            del listacurso[indice]
            print("\nALUNO EXCLUÍDO COM SUCESSO")
        else:
            print('\nAluno não encontrado')
    
    elif op == 3:
        print("-------------------LOCALIZAR ALUNO-------------------------------")
        nome = input("Nome do Aluno: ").upper().strip()
        if nome in listanome:
            indice = listanome.index(nome)
            idade = listaidade[indice]
            curso = listacurso[indice]
            print("")
            print("ALUNO LOCALIZADO COM SUCESSO")
            print("-----------------------------")
            print("Nome:", nome)
            print("Idade:", idade)
            print("Curso:", curso)
            print('------------------------------')
        else:
            print("\nALUNO NÃO CADASTRADO")
    
    elif op == 4:
        for nome, idade, curso in zip(listanome, listaidade, listacurso):
            print("Nome:", nome, "- Idade:", idade, "- Curso:", curso)
