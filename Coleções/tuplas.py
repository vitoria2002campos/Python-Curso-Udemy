"""
Tuplas (Tuple)

Tuplas são muito parecidas com listas.
Existem duas diferenças básicas:
1 - As tuplas são representadas por parenteses()
2 - As tuplas são imutáveis; Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova tupla

#CUIDADO 1: As tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

#CUIDADO 2: Tuplas com 1 elemento

tupla3 = {4} #Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,) #Isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

#CONCLUSÃO: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso de parenteses

(4) -> não é tupla
(4,)-> é tupla
4, -> é tupla

#Podemos gerar uma tupla dinamicamente com range (inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

#Desempacotamento de tupla
tupla = ('Geek University', 'Programação em Python:Essencial')
escola, curso = tupla

#Métodos para: adição, remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutaveis

#Soma, valor maximo, valor minimo e tamanho
#Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

#Concatenação de tuplas
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) #tuplas são imutaveis mas podemos reescrever seus valores

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

#Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(33 in tupla)

#Iterando sobre uma tupla
tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)


#Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

#Dicas na utilização de tuplas
#Devemos utilizar tuplas SEMPRE que precisarmos modificar os dados em uma coleção
#Exemplo 1
meses = ('Janeiro', 'Fevereiro','Março','Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

#O acesso a elementos de uma tupla também é semelhante a de uma lista
print(meses[0])

#Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

#Verificamos em qual indice o elemento está na tupla
print(meses.index('Playstation'))
#OBS: Caso o elemento não exista, será gerado o erro:ValueError: tuple.index(x): x not in tuple

#Slicing
#tupla(inicio:fim:passo)

print(meses[0:]) #Vai me enviar todos os meses
print(meses[5:0])#Vai começar a partir de junho
print(meses[5:9])


#Por que utilizar tuplas?
# - Tuplas são mais rápidas do que listas
# - Tuplas deixam seu código mais seguro
# - Isso porrque trabalhar com elementos imutaveis traz segurança para o código

#Copiando uma tupla para outra
tupla = (1, 2, 3)
print(tupla)
nova = tupla

print(nova)
print(tupla)
"""




