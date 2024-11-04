
resul = []
q=soma = 0

for i in range (10):
 n = int(input("Digite o número para calcular seu quadrado : "))
 q = n**2

 resul.append(q)


soma = sum (resul)
print(resul)
print("Soma dos quadrados dos elementos :",soma)