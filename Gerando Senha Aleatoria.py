#GERANDO SENHA ALEATORIA SEGURA

import random 


numero = random.randint(0,100)
#PERMITE GERAR UM NUMERO ALEATORIO
print(numero)
import secrets 
numero = secrets.choice(range(0,100))
print(numero)
x = secrets.token_bytes(1)
y = secrets.token_hex(1)
z = secrets.token_urlsafe(1)


print(x,y,z)