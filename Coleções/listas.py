"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem dinamicos e também podermos colocar QUALQUER tipo de dado.

 - Dinamico: Não possuem tamanho fixo: Ou seja , podemos criar a lista e simplesmente ir adicionando elementos

 As listas em Python são representadas por colchetes: []

type([])



#Podemos facilmente checar se determinado valor está contido na lista

num = 8

if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o numero {num}')

#Podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)

#Podemos facilmente contar o numero de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

#Adicionar elementos em listas

Para adicionar elementos em listas utilizamos a função append
Com append nós só conseguimos adicionar um elemento por vez
print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8,3,1]) #Coloca a lista como elemento único (sublista)
print(lista1)

lista1.extend([123, 44, 67]) #Coloca cada elemento da lista como valor adicional á lista. O extend não aceita valor único
print(lista1)



#Podemos inserir um novo elemento na lista informando a posição do indice
#OBS: Isso não substitui o valor inicial, o mesmo será deslocado para a direita da lista
lista1.insert(2, 'Novo Valor')
print(lista1)

#Podemos facilmente juntar duas listas

#lista6 = lista1 + lista2

lista1.extend(lista2)
print(lista1)

#Podemos facilmente inverter uma lista
#forma1
lista1.reverse()
lista2.reverse()
#forma2
print(lista1[::-1]) #slice
print(lista2[::-1])


#copiar uma lista
lista6 = lista2.copy()
print(lista6)

print(len(lista1)) #contator de elementos

#Podemos remover o ultimo elemento de uma lista
#OBS: O pop não somente remove o último elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

#Podemos remover o elemento pelo índice
#OBS: Os elementos da direita deste indice deslocados para a esquerda.
#OBS: Se não houver elemento no indice informado, teremos o erro IndexError
lista5.pop(2)
print(lista5)


#Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

#Podemos converter uma string para uma lista
#Exemplo 1
curso = 'Programação em Python Essencial'
curso = curso.split()
print(curso)
#Por padrão, o slipt separa os elementos da lista pelo espaço entre elas.

#Exemplo 2
curso = 'Programação,em,python,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

#Utilizando o While

carrinho= []
produto = ''

while produto != 'sair':
    print("Adicione um na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

    #Utilizando variaveis em listas
numeros = [1, 2, 3, 4, 5]

print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

#Fazemos acesso aos elementos de forma indexada

#           0          1        2       3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) #verde
print(cores[1]) #amarelo
print(cores[2]) #azul
print(cores[3]) #branco

#Outros métodos não são tão importantes mas também úteis
#Encontrar o índice de um elemento na lista

numeros = [5,6,7,8,9,10]

#Em qual índice está o valor 6?
print(numeros.index(6))

#Em qual índice está o valor 9?
print(numeros.index(9))

#Caso não tenha este elemento na lista,  será apresentado erro ValueError
#OBS: Retorna o indice do primeiro elemento encontrado
print(numeros.index(5))

#Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5,1)) #Buscando a partir do índice 1
print(numeros.index(5,2)) #Buscando a partir do índice 2

#|Podemos fazer busca dentro de um range, inicia/fim
print(numeros.index(8, 6, 8))#Buscar o índice do valor 8, entre os índices 3 a 6


#Revisão de slicing
#lista [inicio:fim:passo]
#range [inicio:fim:passo]

#Trabalhando com slice de lista com o parametro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:]) #Iniciando no índice 1 e pegando todos os elementos restantes

#Trabalhando com slice de lista com o parametro 'fim'

print(lista[:2]) #começa em 0, pega até o índice 2 - 1
print(lista[:4]) #começa em 0, pega até o índice 4 - 1
print(lista[1:3])#começa em 1, pega até o índice 3 - 1

#Trabalhando com slice de lista com o parametro 'passo'
print(lista[1::2]) #Comeca em 1, vai até o final, de 2 em 2

print(sum(lista)) #Soma
print(max(lista)) #Máximo valor
print(min(lista)) #Mínimo valor
print(len(lista)) #Tamanho da lista


"""

lista1 = [1,99,4,27,15,22,3,1,44,42,27]
lista2 = ['G', 'e', 'e', 'k', 'u', 'v', 'n', 'i', 'v', 'e', 'r']
lista3 = []
lista4 = list(range(11))
lista5 = list('geek university')



