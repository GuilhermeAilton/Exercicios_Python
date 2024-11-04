import os 
import pandas as pd

lista_arquivo = os.listdir("C:\\Users\\55819\\Downloads\\Vendas\\Vendas")
#Criando uma tabela vazia com pandas
tabela_total = pd.DataFrame()

# PECORRENDO AS PASTAS
for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        print(arquivo)
        tabela = pd.read_csv(f"C:\\Users\\55819\\Downloads\\Vendas\\Vendas\\{arquivo}")
        tabela_total = pd.concat([tabela_total, tabela])

print(tabela_total)
