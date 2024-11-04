'''Faça um programa que receba a temperatura média
de cada mês do ano e armazene-as em uma lista.
Em seguida, calcule a média anual das temperaturas
e mostre a média calculada juntamente com todas as
temperaturas acima da média anual, e em que mês
elas ocorreram (mostrar o mês por extenso: 1 –
Janeiro, 2 – Fevereiro, . '''

meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Novembro,Dezembro']
soma = 0
acima= []
i = 1
temperatura = []
while i < 13 :
   m = float(input("Digite a media do mês {} : ".format(i)))
   temperatura.append(m)
   soma = soma + m
   i += 1
anual = soma /12
  
for m,temperatura in enumerate(temperatura,1) :
    if temperatura > anual :
        acima.append((m,temperatura))



           

  









   





      