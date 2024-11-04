import datetime



from faker import Faker 
fake = Faker() 
print (fake.email()) 
print(fake.country()) 
print(fake.name()) 
print(fake.text()) 
print(fake.latitude(), fake.longitude()) 
print(fake.url()) 
print(fake.generator_attrs[7])



data = datetime.datetime.today().strftime('%d/%m/%y').s


if data == '22/08/23':
    print('Feliz dia dos pais')

else:
    print('Obrigado')


