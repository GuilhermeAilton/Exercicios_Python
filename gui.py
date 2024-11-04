alunos = ['Artur', 'Caio', 'Bruna', 'Flávia', 'Manoel', 'Tatiana']
notas = [10, 6, 7.5, 3, 8, 9.4]

nome = input("Digite o nome do aluno: ")

if nome in alunos:
    indice = alunos.index(nome)
    nota = notas[indice]
    print(f"A nota de {nome} é {nota:.2f}")
else:
    alunos.append(nome)
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)
    print(f"Novo aluno: {nome}")
    print(f"Nota: {nota:.2f}")