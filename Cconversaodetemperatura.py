ent = input('')
sai = input('')
temp = int (input(''))

if ent == 'celsius' and sai == 'fahrenheit' :
    con = 9/5 * temp + 32
    print("Valor convertido para Fahrenheit",con,"Fahrenheit")

if ent == 'celsius' and sai == 'kelvin' :
    con = temp + 273.15
    print("Valor convertido para Kelvin :",con,"Kelvin")

if ent == 'fahrenheit' and sai  == 'celsius':
    con = 5/9 * temp - 32
    print("Valor convertido para Celsius",con,"°") 

if ent =='fahrenheit' and sai == 'kelvin':
    con = 5/9 * (temp - 32) + 273.15  

if ent == 'kelvin' and sai == 'celsius':
    con = temp - 273.15
    print("Valor convertido para Celsius",con,"°")

if ent == 'kelvin' and sai == 'fahrenheit' :
    con = 9/5 * (temp - 273.15) + 32
    print("Valor convertido para Fahrenheit",con,"kelvin")

   