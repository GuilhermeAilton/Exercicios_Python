def criar_conta(numero,titular,saldo,limite):
    conta = {'Número:',numero,'Nome : ','Titular: ',titular,'Saldo: ',saldo,'Limite : ',limite }
    return conta
def deposita(conta,valor) :
    conta['saldo'] += valor 
    return conta

def saca (conta,valor) :
    conta['saldo]