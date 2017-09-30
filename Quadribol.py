import random

def randomList(sizeList , list):
    for i in range(sizeList):
        Check = True
        while Check:
            list[i] = int(((sizeList) * random.random()) + 1)
            for j in range(sizeList):
                if j == i:
                    continue
                if list[i] == list[j]:
                    list[i] = 0
            if list[i] < 1:
                continue
            Check = False
    return list

""""
    TODO: refatorar todas a lista para o limite de 16 elementos
"""

answer = "Nada"
custom = False
teams = [0 for i in range(17)]
timesnochamp = 4
nExiste = True
names1y2 = [[" ", "Mandragor", "Céu", "Salgueiro", "Farrapo", "O Trazgo", "Bjørner", "Névoa", "Hipogrifo",
             "Licantropo", "Fado", "Ricochete", "Relampago", "Gavião", "Mago", "Elfo", "Goblin"],
            [" ", "Alado", "da Floresta", "Prateado", "Terrível", "de Merlin", "Negro", "Silencioso", "Ardente",
             "Poderoso", "Verde", "Esquecido", "de Ouro", "Azul", "Feroz", "Defensivo", "Rubro"]]

print('<==========Campeonato de Quadribol!==========>')
answer = input(('Você quer customizar o jogo escolhendo times e etc?\n'))

if answer == "Sim" or answer == "sim" or answer == "aham" or answer == "Aham" or answer == "claro" or answer == "Claro":
    custom = True

if custom:
    timesnochamp = int(input(('Quantos times estarão em jogo? o máximo é 16.\n')))
else:
    timesnochamp = 4

chaves = int(timesnochamp/2)

print('\nA quantidade de times no jogo serão: {}.\nE a quantidade de chaves vai ser: {}.\n'
      .format(timesnochamp, chaves))

for i in range(timesnochamp):
    nExiste = True
    while nExiste:
        teams[i] = int(((timesnochamp) * random.random())+1)
        for j in range(timesnochamp):
            if j == i:
                continue
            if teams[i] == teams[j]:
                teams[i] = 0
        if teams[i] < 1:
            continue
        nExiste = False

# Confere lista random
#for i in range(timesnochamp):
#    print(teams[i])


listaUm = [0 for i in range(17)]
listaDois = [0 for i in range(17)]
listaUm = randomList(timesnochamp, listaUm)
listaDois = randomList(timesnochamp, listaDois)

# Confere listaUm e listaDois
#print(listaUm)
#print(listaDois)


nomesTimes = [0 for i in range(16)]
for i in range(timesnochamp):

    nomesTimes[i] = names1y2[0][listaUm[i]] + ' ' + names1y2[1][listaDois[i]]

aux1 = 1
aux2 = 2

for i in range(chaves):
    print('            /\'- {}\nChave x <=={{\n            \.- {}\n\n'.format(nomesTimes[aux1], nomesTimes[aux2]))
    aux1 += 2
    aux2 += 2













