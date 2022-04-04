"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários são conhecidos por mapas

Dicionários são representados por chaves {}

print(type({}))
    - chave e valor são separados por dois pontos 'chave:valor'
    - Tanto chave e valor podem ser de qualquer tipo de dado:
    - Podemos misturar tipos de dados:

    #Criação de dicionários
#Forma 1 (Comum) RECOMENDADA
paises = {'br':'Brasil','eua':'Estados Unidos','py':'Paraguai'}

print(paises)
print(type(paises))

#Forma 2 (Não comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

#Acessando elementos
paises = {'br':'Brasil','eua':'Estados Unidos','py':'Paraguai'}

#Forma 1 - Acessando via chave da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])
#print(paises['ru'])
#OBS: Caso tentamos fazer o acesso de uma chave que não existe, teremos o KeyError

#Forma 2 - Acessando via get - Recomendado
print(paises.get('br'))
print(paises.get('ru'))


#Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError
pais= paises.get('ru')

if pais:
    print('Encontrei o país {pais}')
else:
    print('Não encontrei o país')

#Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('ru', 'Não encontrado')
print(f'Encontrei o país {pais}')
print(f'Encontrei o pais {pais}')

paises = {'br':'Brasil','eua':'Estados Unidos','py':'Paraguai'}

#Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']
"""


