
#Não	é	possível	acessar	um	elemento	de	um	dicionário	por	um	índice	como	na	lista.	Devemos	acessálos	por	sua	chave:
pessoa={'nome':'João',	'idade':25,	'cidade':'São Paulo'}
print(pessoa['nome'])

# ADICIONAR UM ELEMENTO DICIONARIO
pessoa['pais'] = 'BRASIL'
print(pessoa)
pessoa ['nome'] = ' Guilherme'
print(pessoa.keys())
print(pessoa.values())

#Retorna todos os valores e chaves relacionadas i
print(pessoa.items())

#GET Pega o conteúdo de cada chave.
print(pessoa.get())