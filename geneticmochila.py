from random import randint, random, choices
from operator import add
from functools import reduce

def individual(length):
    'Create a member of the population.'
    #é selecionado de forma aleatoria se vai conter ou não o item da posição x
    return [ randint(0,1) for x in range(length) ]

def population(count, catalogo):
    #Cria uma população com base no tipo de cátalogo de itens disponíveis
    return [ individual(len(catalogo)) for x in range(count) ]

def fitness(individual, catalogo, target):
    #Quanto mair o valor melhor, se peso maior que o limite, valor é 0
    peso = 0
    valor = 0
    index = 0
    for item in individual:
        if item == 1:
            peso = peso + catalogo[index]["peso"]
            valor = valor + catalogo[index]["valor"]
        index = index + 1

    if peso > target:
        valor = 0

    return abs(valor)

def media_fitness(pop, catalogo, target):
    'Find average fitness for a population.'
    summed = reduce(add, (fitness(x, catalogo, target) for x in pop))
    return summed / (len(pop) * 1.0)

def evolve(pop, catalogo, target, mutate=0.01):
    #Calcular o fitness total
    summed = reduce(add, (fitness(x, catalogo, target) for x in pop))

    #Calcular porcentagem individual
    porcentagem = []
    for x in pop:
        p = fitness(x, catalogo, target) / summed
        porcentagem.append(p)


    #descobre quantos filhos terao que ser gerados
    desired_length = len(pop)
    children = []
    #comeca a gerar filhos
    while len(children) < desired_length:
        #Escolhe pai e mae por roleta'
        pais = choices(
            population=pop,
            weights=porcentagem,
            k=2
        )
        male = pais[0]
        female = pais[1]
        if male != female:
            half = len(male) // 2
            #gera filho metade de cada
            child = male[:half] + female[half:]

            #Mutação
            if mutate > random():
                gene_mutado = randint(0,len(catalogo)-1)
                if child[gene_mutado] == 1:
                    child[gene_mutado] = 0
                else:
                    child[gene_mutado] = 1

            #adiciona novo filho a lista de filhos
            children.append(child)


    return children
