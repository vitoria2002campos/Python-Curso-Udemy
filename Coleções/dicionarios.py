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

#Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

#Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionário, como chaves de dicionários.

#Tuplas por exempo são muito interessantes de serem usadas como chaves de dicionários, pois elas são imutáveis

localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

#Adicionar elementos em um dicionário

receita = {'jan':100, 'fev':120, 'mar':300,}

print(receita)
print(type(receita))

#Forma 1 (Comum)
receita['abr'] = 350
print(receita)

#Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado) #receita.update({'mai' :500})
print(receita)

#Atualizando dados em um dicionário

#Forma 1
receita['mai'] = 550
print(receita)

#Forma 2
receita.update({'mai':600})
print(receita)
#CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma
#CONCLUSÃO 2: Em dicionários , NÃO podemos ter chaves repetidas

#Como remover dados de um dicionário

receita = {'jan':100, 'fev':120, 'mar':300,}

print(receita)
#Forma 1 (Comum)
ret = receita.pop('mar') #ret de retorno
print(ret)
print(receita)
#OBS:Aqui precisamos sempre informar a chave, e caso não encontre o elemento, um KeyError é retornado
#OBS: Ao removermos um objeto, o valor desse objeto é sempre retornado

#Forma 2

del receita ['fev']
print(receita)

#Se a chave não existir será gerado um KeyError
#OBS: Neste caso o valor removido não é retornado
"""

#Imagine que voce tem um comércio eletronico, onde temos um carrinho de compras na qual adicionamos produtos
"""
Carrinho de Compras
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;
        

#Poderiamos utilizar uma lista para isso? Sim

carrinho = []

produto1 = ['Playstation 4','1',230.00]
produto2 = ['God of war 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

#Teriamos que saber qual é o índice de cada informação no produto
# 2 , poderiamos utilizar umatupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.0 )
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)

#Poderiamos utilizar um dicionário para isso? Sim

carrinho = []

produto1 = {'nome':'Playstation 4', 'quantidade':1, 'preco':2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade':1,'preco': 150.00 }

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
#Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter a certeza sobre cada informação


#Métodos de dicionários.

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

#Limpar o dicionário (Zerar dados)
d.clear()
print(d)

#Copiando um dicionário para outro

#Forma 1

novo = d.copy() #Deep Copy
print(novo)

novo['d'] = 4
print(d)
print(novo)

#Forma 2 # Shallow Copy

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

novo = d
print(novo)

novo['d'] = 4

print(d)
print(novo)


#Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))
#O método fromKeys recebe dois parametros: um iterável e um valor.
#Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1,11, 'novo'))
print(veja)
"""
