p = float(input(""))
q1 = int (input(""))
q2 = int (input(""))
q3 = int (input(""))
q4 = int (input(""))
q5 = int (input(""))

valor= q1 * 1 +  q2 * 0.50 + q3 * 0.25 +  q4 * 0.10 + q5 * 0.05
valor = (round (valor,2))
if p == valor :
 print("%.2f" % valor)     
 print("Produto pago")
 
if p > valor :
 print(valor)
 total = p - valor 
 total = round(total,2)
 print(f"Valor insuficiente, faltam {total:.2f}")
if  valor > p :
 print(valor) 
 total = valor - p 
 print(f"Produto pago, o troco é de {total:.2f}")
 
