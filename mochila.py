from geneticmochila import *

itensDisponiveis = [
    { "peso": 1,    "valor": 80     },
    { "peso": 2,    "valor": 40     },
    { "peso": 2,    "valor": 90     },
    { "peso": 1,    "valor": 10     },
    { "peso": 5,    "valor": 30     },
    { "peso": 4,    "valor": 100    },
    { "peso": 1,    "valor": 5      },
    { "peso": 10,   "valor": 200    },
    { "peso": 3,    "valor": 30     },
    { "peso": 3,    "valor": 25     },
    { "peso": 2,    "valor": 27     },
    { "peso": 1,    "valor": 9      },
    { "peso": 1,    "valor": 21     },
    { "peso": 5,    "valor": 60     },
    { "peso": 3,    "valor": 20     },
]

#peso max em kg
peso_max = 20

#tamanho da população
p_count = 100

#quantidade de gerações
epochs = 3000

#criar população
p = population(p_count, itensDisponiveis)


fitness_history = [media_fitness(p, itensDisponiveis, peso_max),]

print (fitness_history)


for i in range(epochs):
    p = evolve(p, itensDisponiveis, peso_max)
    fitness_history.append(media_fitness(p, itensDisponiveis, peso_max))

for datum in fitness_history:
   print (datum)
