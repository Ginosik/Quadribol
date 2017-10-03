import random


def randomList(sizeList):
    auxList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(sizeList):
        Check = True
        while Check:
            auxList[i] = int(((sizeList) * random.random()) + 1)
            for j in range(sizeList):
                if j == i:
                    continue
                if auxList[i] == auxList[j]:
                    auxList[i] = 0
            if auxList[i] < 1:
                continue
            Check = False
    auxList.remove(0)
    return auxList

def introQuadribol():
    bResp = False
    print('<==========Campeonato de Quadribol!==========>')
    strResp = input('Você quer customizar o jogo escolhendo times e etc?\n')

    if strResp == "Sim" or answer == "sim" or answer == "aham" or answer == "Aham" or answer == "claro" or answer == "Claro":
        bResp = True

    return bResp

""""
    TODO: elaborar resolução do campeonato
            ->transformar particulas em funções
                ->corrigir bug no introQuadribol
"""

answer = ""
custom = False
teams = []
timesnochamp = 4
nExiste = True
names1y2 = [["Mandragor", "Céu", "Salgueiro", "Farrapo", "O Trazgo", "Bjørner", "Nevoeiro", "Hipogrifo",
             "Licantropo", "Fado", "Ricochete", "Relampago", "Gavião", "Mago", "Elfo", "Goblin"],
            ["Alado", "da Floresta", "Prateado", "Terrível", "de Merlin", "Negro", "Silencioso", "Ardente",
             "Poderoso", "Verde", "Esquecido", "de Ouro", "Azul", "Feroz", "Defensivo", "Rubro"]]

custom = introQuadribol()

if custom:
    timesnochamp = int(input(('Quantos times estarão em jogo? o máximo é 16.\n')))
    if timesnochamp > 16:
        print("Desculpe, o número máximo de times é 16. Vamos seguir com 16.\n")
        timesnochamp = 16
    if timesnochamp < 2:
        print("Desculpe, o número mínimo de times é 2. Vamos seguir com 2.\n")
        timesnochamp = 2
else:
    timesnochamp = 4

chaves = int(timesnochamp / 2)

print('\nA quantidade de times no jogo serão: {}.\nE a quantidade de chaves vai ser: {}.\n'
      .format(timesnochamp, chaves))

teams = randomList(timesnochamp)

'''
# Confere lista random
for i in range(timesnochamp):
    print(teams[i])
'''

listaUm = []
listaDois = []
listaUm = randomList(timesnochamp)
listaDois = randomList(timesnochamp)

'''
# Confere listaUm e listaDois
# print(listaUm)
# print(listaDois)
'''

nomesTimes = []
nomesTimes = randomList(timesnochamp)

for i in range(timesnochamp):
    nomesTimes[i] = names1y2[0][listaUm[i]-1] + ' ' + names1y2[1][listaDois[i]-1]

aux1 = 0
aux2 = 1

numeroChave = 1

for i in range(chaves):
    print('            /\'- {}\nChave {} <=={{\n            \.- {}\n\n'.format(nomesTimes[aux1], numeroChave,
                                                                               nomesTimes[aux2]))
    numeroChave += 1
    aux1 += 2
    aux2 += 2
