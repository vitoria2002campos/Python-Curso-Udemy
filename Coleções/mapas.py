"""
Mapas conhecidos em python como dicionários

Dicionários em Python são representados por chaves {}



#Interar sobre dicionários


for chave in receita:
#printa somente as chaves
    print(chave)

for chave in receita:
#printa somente os valores
    print(receita[chave])

for chave in receita:
print(f'{chave}:{receita[chave]}')
    #printa a chave e o valor



for chave in receita:
    print (f'Em {chave} recebi R$ {receita[chave]}')


#ACESSANDO AS CHAVES
print(receita.keys()) #.keys dicionario de chaves

for chave in receita.keys(): #modo pythonico
    print (receita[chave])

#ACESSANDO OS VALORES

print(receita.values()) #.values Dicionário de valores

for valor in receita.values():
    print(valor) #modo pythonico de fazer acesso aos valores
"""

receita = {'jan':100, 'fev':250, 'mar':400}
print(receita)


#desempacotamento de dicionários

for chave, valor in receita.items():
    print(f' chave=({chave} e valor={valor})')

#Soma, Valor max, Valor min, tamanho
#Se os valores forem inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))