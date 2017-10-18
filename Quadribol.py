import random

class Partida:
    victory = 0
    rodada = 0
    blabla = ("1","2")
    

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
    if strResp == "Sim" or strResp == "sim" or strResp == "aham" or strResp == "Aham" or strResp == "claro" or strResp == "Claro":
        bResp = True
    return bResp

def howToPontos():
    bHowToPontos = False
    strResp = input("Quer saber como o sistema de pontuação funciona?\n")
    if strResp == "Sim" or strResp == "sim" or strResp == "aham" or strResp == "Aham" or strResp == "claro" or strResp == "Claro":
        bHowToPontos = True
    return bHowToPontos

def chooseNumberOfTeams(custom):
    timesnochamp = 0
    if custom:
        timesnochamp = int(input(('Quantos times estarão em jogo? O máximo é 16.\n')))
        if timesnochamp > 16:
            print("Desculpe, o número máximo de times é 16. Vamos seguir com 16.\n")
            timesnochamp = 16
        if timesnochamp < 2:
            print("Desculpe, o número mínimo de times é 2. Vamos seguir com 2.\n")
            timesnochamp = 2
    else:
        timesnochamp = 4
    return timesnochamp

""""
    TODO: elaborar resolução do campeonato
            ->transformar particulas em funções
"""
'''Variáveis'''
custom = False
teams = []
timesnochamp = 4
nExiste = True
restante = False
names1y2 = [["Mandragor", "Céu", "Salgueiro", "Farrapo", "O Trazgo", "Bjørner", "Nevoeiro", "Hipogrifo",
             "Licantropo", "Fado", "Ricochete", "Relampago", "Gavião", "Mago", "Elfo", "Goblin"],
            ["Alado", "da Floresta", "Prateado", "Terrível", "de Merlin", "Negro", "Silencioso", "Ardente",
             "Poderoso", "Verde", "Esquecido", "de Ouro", "Azul", "Feroz", "Defensivo", "Rubro"]]




custom = introQuadribol()

timesnochamp = chooseNumberOfTeams(custom)

if custom:
    howToPontos = howToPontos()
    if howToPontos:
        print('Muito bem! Para cada gol marcado por um dos jogadores serão somados 10 pontos ao placar.\n'
              'Pegando o pomo de ouro são somados 30 pontos e o jogo é finalizado.')
        input("\n\nAperte Enter para continuar...")

if False != (timesnochamp %2):
    restante = True
chaves = int(timesnochamp / 2)

print('\nA quantidade de times no jogo serão: {}.\nE a quantidade de chaves vão ser: {}.\n'
      .format(timesnochamp, chaves))

teams = randomList(timesnochamp)

listaUm = []
listaDois = []
listaUm = randomList(timesnochamp)
listaDois = randomList(timesnochamp)

nomesTimes = []
nomesTimes = randomList(timesnochamp)

for i in range(timesnochamp):
    nomesTimes[i] = names1y2[0][listaUm[i]-1] + ' ' + names1y2[1][listaDois[i]-1]

aux1 = 0
aux2 = 1

numeroChave = 1

if  True != (timesnochamp % 2):
    print('numero par de times\n')
else:
    print('numero impar de times\n')

    print("um time sorteado irá para a próxima etapa automaticamente: ", nomesTimes[-2],'\n')

for i in range(chaves):
    print('            /\'- {}\nChave {} <=={{\n            \.- {}\n'.format(nomesTimes[aux1], numeroChave,
                                                                               nomesTimes[aux2]))
    numeroChave += 1
    vencedor = int(2 *random.random())
    if(vencedor):
        vencedor = nomesTimes[aux1]
    else:
        vencedor = nomesTimes[aux1]
    aux1 += 2
    aux2 += 2

    print("O vencedor da rodada foi: " , vencedor, "\n\n")


listTest = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while(timesnochamp != 1):
    restante = 0
    print(timesnochamp)
    if(True !=(timesnochamp %2)):
        timesnochamp //= 2
    else:
        timesnochamp //= 2
        restante = 1
        timesnochamp +=restante

