from math import e, sqrt
from random import randint, shuffle
from time import sleep, time

def order_map(key, value, x = 2):
  if len(key) != len(value):
    return "Error in length of key and value"
  while x != 0 and x != 1:
    x = int(input("Ordem crescente -> 0 | decrescente -> 1:\n"))
    if (x > 1 or x < 0):
      print("Try again:")
  ordenator = []
  copia = []
  for i in range(len(value)):
    copia.append(value[i])
  menor = value[0]
  for i in range(1,len(value)):
    if menor > value[i]:
      menor = value[i]
  for j in range(len(key)):
    maior = menor
    for i in range(len(value)):
      if maior <= value[i]:
        maior = value[i]
        index = i
    ordenator.append(index)
    value[index] = menor-1
  for i in range(len(copia)):
    value[i] = copia[i]
  k = []
  v = []
  for i in range(len(key)):
    k.append(key[ordenator[i]])
    v.append(value[ordenator[i]])
  for i in range(len(k)):
    if x == 0:
      key[i] = k[len(k)-i-1]
      value[i] = v[len(v)-i-1]
    else:
      key[i] = k[i]
      value[i] = v[i]

debug = False
if debug:
    lightSpeed = True
else:
    while True:
        numModos = 7
        a = input("Qual modo deseja jogar?\n[BRASILEIRAO] = 0\n[PREMIER LEAGUE] = 1\n[BUNDESLIGA] = 2\n[AMISTOSO] = 3\n[SIMULACAO BRASILEIRAO] = 4\n[SIMULACAO PREMIER LEAGUE] = 5\n[SIMULACAO BUNDESLIGA] = 6\n")
        if a == '0' or a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a == '6':
            break
        else:
            print("Valor invalido! Tente novamente...")
    a = int(a)
    lightSpeed = False
    if a > (numModos-1)/2:
        lightSpeed = True
    amistoso = False
    if a == (numModos-1)/2:
        amisoso = True

gols = 0
jogos = 0
# power premier league *= 1.26309
# power bundesliga *= 1.07231
times =         ['FLAMENGO',    'SANTOS',   'PALMEIRAS',    'GREMIO',   'ATHLETICO-PR', 'SAO PAULO',    'INTERNACIONAL',    'CORINTHIANS', 'FORTALEZA', 'GOIAS',    'BAHIA',    'VASCO',    'ATLETICO-MG',  'FLUMINENSE',   'BOTAFOGO', 'CEARA',    'CRUZEIRO', 'CSA',      'CHAPECOENSE',  'AVAI',     'LIVERPOOL',   'MANCHESTER CITY',      'LEICESTER',    'CHELSEA',      'MANCHESTER UNITED',    'WOLVERHAMPTON',    'SHEFFIELD UNITED', 'TOTTENHAM',    'ARSENAL',  'BURNLEY',  'CRYSTAL PALACCE',  'EVERTON',  'NEWCASTLE',    'SOUTHAMPTON',  'BRIGHTON', 'WEST HAM', 'WATFORD',  'BOURNEMOUTH',  'ASTON VILLA',  'NORWICH',   'BAYERN MUNCHEN',   'DORTMUND', 'LEIPZIG',  'MONCHENGLADBACH',  'BAYER LEVERKUSEN', 'SCHALKE 04',   'WOLFSBURG',    'FREIBURG', 'HOFFENHEIM',   'KOLN',     'UNION BERLIN', 'EINTRACHT FRANKFURT',  'HERTHA BERLIN',    'AUGSBURG', 'MAINZ 05', 'DUSSELDORF',   'WERDER BREMEN',    'PADERBORN 07'  ]
power =         [2.32432,       1.81818,    1.90625,        1.64103,    1.59375,        1.3,            1.12821,            1.2353,        1.02041,     0.71875,    1.02326,    0.86667,    0.91837,        0.82609,        0.68889,    0.87805,    0.58696,    0.41379,    0.59615,        0.29032,    3.96971,       2.77065,                2.61640,        1.65173,        1.85253,                1.52314,            1.51571,            1.48413,        1.40343,    1.07363,    1.02626,            1.01596,    0.77018,        0.85016,        1.01047,    0.88416,    0.77508,    0.77935,        0.76688,        0.60725,     3.01072,            2.20961,    2.55705,    1.75144,            1.60847,            0.98295,        1.21528,        1.04167,    0.87281,        0.92934,    0.83692,        0.99385,                0.71487,            0.74237,    0.68790,    0.57905,        0.52641,            0.59573         ]
offensiveness = [2.20361,       1.37119,    1.3518,         1.72853,    1.13019,        0.81025,        1.18837,            0.98892,       1.69668,     2.03878,    1.31025,    1.21537,    1.52701,        1.21053,        0.96607,    1.02216,    0.86011,    0.96399,    1.11634,        0.77285,    1.64804,       2.68878,                1.93103,        2.36504,        1.56956,                1.65755,            0.95663,            2.23543,        1.83673,    1.61712,    0.98930,            2.02378,    1.21879,        2.16409,        1.52200,    2.08086,    1.41260,    1.62069,        2.42857,        1.54578,     3.03680,            3.59040,    2.57920,    2.35200,            2.16000,            1.90080,        1.63200,        1.90400,    2.40800,        2.80800,    2.09920,        2.70486,                2.45760,            2.99520,    2.88320,    2.16000,        2.57813,            2.59200         ]
vogal =         ['o',           'o',        'o',            'o',        'o',            'o',            'o',                'o',            'o',        'o',            'o',    'o',            'o',        'o',            'o',        'o',        'o',        'o',        'a',            'o',        'o',           'o',                    'o',            'o',            'o',                    'o',                'o',                'o',            'o',        'o',        'o',                'o',        'o',            'o',            'o',        'o',        'o',        'o',            'o',            'o',         'o',                'o',        'o',        'o',                'o',                'o',            'o',            'o',        'o',            'o',        'o',            'o',                    'o',                'o',        'o',        'o',            'o',                'o'             ]
mediaPontos = []
atk = []
defense = []
fieldFactor =   []
# fieldFactorBrasileirao = 20%
# fieldFactorPremier = 11%
# fieldFactorBundesliga = 8%
for i in range(len(times)):
    if i < 20:
        fieldFactor.append(0.2)
    elif i < 40:
        fieldFactor.append(0.11)
    else:
        fieldFactor.append(0.08)
for i in range(len(times)):
    atk.append( sqrt( offensiveness[i] * power[i] ) )
    defense.append( sqrt( offensiveness[i]/(power[i]*1.0) ) )
mediaGolsBrasileirao    =  3.297 # Por meio de simulacoes, com esse valor chegamos em 2.305 gols por partida em media ¯\_(ツ)_/¯
mediaGolsPremierLeague  =  2.774 # Por meio de simulacoes, com esse valor chegamos em 2.722 gols por partida em media ¯\_(ツ)_/¯
mediaGolsBundesliga     =  2.340 # Por meio de simulacoes, com esse valor chegamos em 3.250 gols por partida em media ¯\_(ツ)_/¯
atkMedioBrasileirao = 2 * sum(atk)/len(atk) * sum(atk)/len(atk) / mediaGolsBrasileirao
defenseMedioBrasileirao = 2 * sum(defense)/len(defense) * sum(defense)/len(defense) / mediaGolsBrasileirao
atkMedioPremierLeague = 2 * sum(atk)/len(atk) * sum(atk)/len(atk) / mediaGolsPremierLeague
defenseMedioPremierLeague = 2 * sum(defense)/len(defense) * sum(defense)/len(defense) / mediaGolsPremierLeague
atkMedioBundesliga = 2 * sum(atk)/len(atk) * sum(atk)/len(atk) / mediaGolsBundesliga
defenseMedioBundesliga = 2 * sum(defense)/len(defense) * sum(defense)/len(defense) / mediaGolsBundesliga

for i in range(len(times)):
    if i < 20:
        atk[i] = atk[i] / sqrt(atkMedioBrasileirao)
        defense[i] = defense[i] / sqrt(defenseMedioBrasileirao)
    elif i < 40:
        atk[i] = atk[i] / sqrt(atkMedioPremierLeague)
        defense[i] = defense[i] / sqrt(defenseMedioPremierLeague)
    else:
        atk[i] = atk[i] / sqrt(atkMedioBundesliga)
        defense[i] = defense[i] / sqrt(defenseMedioBundesliga)

if a%((numModos+1)/2) == 0:
    times =         times[:20]
    power =         power[:20]
    offensiveness = offensiveness[:20]
    atk =           atk[:20]
    defense =       defense[:20]

elif a%((numModos+1)/2) == 1:
    times =         times[20:40]
    power =         power[20:40]
    offensiveness = offensiveness[20:40]
    atk = atk[20:40]
    defense = defense[20:40]

elif a%((numModos+1)/2) == 2:
    times =         times[40:]
    power =         power[40:]
    offensiveness = offensiveness[40:]
    atk =           atk[40:]
    defense =       defense[40:]

for i in times:
    mediaPontos.append(0)

print()
aux = times[:]
auxAtk = atk[:]
auxDefense = defense[:]
auxRatio = []
for i in range(len(times)):
    auxRatio.append(atk[i]/defense[i])
temp = auxRatio[:]
order_map(aux, temp, 1)
temp = auxRatio[:]
order_map(auxAtk, temp, 1)
temp = auxRatio[:]
order_map(auxDefense, temp, 1)
for i in range(len(times)):
    print("{:.2f} | {:.2f} ->\t{}".format(auxAtk[i], auxDefense[i], aux[i]))
print()
    
gramaticaCampeao = []
for letra in vogal:
    if letra == 'a':
        gramaticaCampeao.append('')
    else:
        gramaticaCampeao.append('o')

vezesCampeao = []
for num in times:
    vezesCampeao.append(0)

while True:
    if lightSpeed:
        gameMode = 1
        break
    else:
        gameMode = input("Escolha modo de jogo: [PADRAO] = 0 | [TURBO] = 1\n")
        if gameMode == '0' or gameMode == '1':
            break
        else:
            print("Valor invalido! Tente novamente...\n")
gameMode = int(gameMode)

def fat(y):
    if y == 0:
        return 1
    num = 1
    dec = y
    while dec-1:
        num *= dec
        dec -= 1
    return num

def findIndex(x):
    for i in range(len(times)):
        if times[i] == x.upper():
            return i
    return -1

def findLambda(A, B, neutrality, extraTime = False):
    indexA = findIndex(A)
    indexB = findIndex(B)
    if not neutrality:
        homeFactor = sqrt(1 + fieldFactor[indexA]) * sqrt(1 + fieldFactor[indexB])
        awayFactor = sqrt(1 - fieldFactor[indexA]) * sqrt(1 - fieldFactor[indexB])
    else:
        homeFactor = 1
        awayFactor = 1
    lambdaA = atk[indexA] * defense[indexB] * homeFactor
    lambdaB = atk[indexB] * defense[indexA] * awayFactor
    if extraTime:
        lambdaA = lambdaA / 3.0
        lambdaB = lambdaB / 3.0
    else:
        if not lightSpeed and not gameMode:
            print("Resultado esperado: {} {:.2f} vs {:.2f} {}\n".format(A, lambdaA, lambdaB, B))
    return lambdaA, lambdaB

def draftGoal(lista):
    newList = []
    for i in range(len(lista)):
        for j in range(int(lista[i])):
            newList.append(i)
    rnd = randint(0,len(newList)-1)
    return newList[rnd]

def poisson(A, B, neutrality, extraTime = False):
    lambdaA, lambdaB = findLambda(A, B, neutrality, extraTime)
    P1 = []
    P2 = []
    for i in range(9):
        result = (e**(-1*lambdaA) * lambdaA**i) / (fat(i)*1.0)
        P1.append(1000*result)
        result = (e**(-1*lambdaB) * lambdaB**i) / (fat(i)*1.0)
        P2.append(1000*result)
    golsA = draftGoal(P1)
    golsB = draftGoal(P2)
    return golsA, golsB

def match(pontos, mediaPontos, A, B, grupo, neutrality, amistoso, lastGame = True, knockOut = False):
    if not lightSpeed and not gameMode:
        print("\n========================================================================================================================\n")
        print("\nPARTIDA:", A.upper(), "x", B.upper())
        print()
    if not gameMode:
        sleep(1.5)
    golsA, golsB = poisson(A, B, neutrality)
    if not lightSpeed:
        goalStamps = []
        sideScoring = []
        for i in range(golsA):
            sideScoring.append(0)
        for i in range(golsB):
            sideScoring.append(1)
        for i in range(golsA + golsB):
            while True:
                stamp = randint(1,90)
                if stamp not in goalStamps:
                    goalStamps.append(stamp)
                    break
        shuffle(sideScoring)
        count = 0
        placarA = 0
        placarB = 0
        for tempo in range(1, 91):
            if tempo in goalStamps:
                if sideScoring[count]:
                    placarB += 1
                else:
                    placarA += 1
                if not gameMode:
                    goalEvent(A, B, sideScoring[count], placarA, placarB, tempo)
                count += 1
            else:
                if not gameMode:
                    otherEvents(A, B, tempo)
            if not gameMode:
                sleep(0.1)
    if lightSpeed:
        global jogos, gols
        jogos += 1
        gols = gols + golsA + golsB
    if not knockOut:
        indexA = findIndex(A)
        indexB = findIndex(B)
        if golsA > golsB:
            pontos[indexA] = pontos[indexA] + 3 + 0.0001*(golsA-golsB) + 0.00000001*golsA
            pontos[indexB] = pontos[indexB] + 0.01 + 0.0001*(golsB-golsA) + 0.00000001*golsB
        elif golsB > golsA:
            pontos[indexB] = pontos[indexB] + 3 + 0.0001*(golsB-golsA) + 0.00000001*golsB
            pontos[indexA] = pontos[indexA] + 0.01 + 0.0001*(golsA-golsB) + 0.00000001*golsA
        else:
            pontos[indexA] = pontos[indexA] + 1 + 0.00000001*golsA
            pontos[indexB] = pontos[indexB] + 1 + 0.00000001*golsB

    if not lightSpeed:
        print("FINAL DE PARTIDA:",A.upper(),golsA,'x',golsB,B.upper())
    if not knockOut and not amistoso and lastGame:
        showTable(pontos, mediaPontos, grupo)
    if not gameMode:
        input("\nPartida terminada. Pressione ENTER para continuar...")
    if not lightSpeed:
        print()

def otherEvents(A, B, tempo):
    rnd = randint(0,1)
    if rnd:
        randomTeam = B.upper()
        index = findIndex(B)
    else:
        randomTeam = A.upper()
        index = findIndex(A)
    event = randint(1, 1350)
    if event == 1:
        print("Que situacao! Torcedor revoltado entra em campo pra protestar aos", tempo, "minutos, mas eh detido a tempo!\n")
    elif event < 4:
        print("Bandeirinha atento! {}".format(vogal[index].upper()), randomTeam, "ja ia marcando um gol aos", tempo, "minutos, mas o artilheiro tava na banheira.\n")
    elif event < 56:
        print("Falta pr{}".format(vogal[index]), randomTeam, "cobrar. Jogador adversario tomou o amarelo aos", tempo, "minutos de jogo.\n")
    elif event < 61:
        print("Expulso o defensor d{}".format(vogal[index]), randomTeam, "depois de uma falta dura aos", tempo, "minutos!\n")

def goalEvent(A, B, side, placarA, placarB, tempo):
    if not side:
        timeGol = A.upper()
        index = findIndex(A)
    else:
        timeGol = B.upper()
        index = findIndex(B)
    tipo = randint(0,100)
    if tipo == 0:
        print("Ih rapaz... O goleirao falhou! Entregou pr{}".format(vogal[index]), timeGol, "marcar aos", tempo, "minutos!")
    elif tipo < 21:
        print("Gol de escanteio d{}".format(vogal[index]), timeGol, "aos", tempo, "minutos!")
    elif tipo < 41:
        print("Gol de cabeca d{}".format(vogal[index]), timeGol, "aos", tempo, "minutos!")
    elif tipo < 56:
        print("Golaco de longe d{}".format(vogal[index]), timeGol, "aos", tempo, "minutos!")
    elif tipo < 81:
        print("Golaco! Jogada trabalhada d{}".format(vogal[index]), timeGol, "aos", tempo, "minutos!")
    elif tipo < 91:
        print("Gol de puro talento em jogada individual d{}".format(vogal[index]), timeGol, "aos", tempo, "minutos!")
    elif tipo < 96:
        print("Golaco de falta d{}".format(vogal[index]), timeGol, "aos", tempo, "minutos!")
    else:
        print("Gol de penalti d{}".format(vogal[index]), timeGol, "aos", tempo, "minutos!")
    print(A.upper(), placarA, "x", placarB, B.upper())
    print()

def showTable(pontos, mediaPontos, grupo, fim = False):
    try:
        timesGrupo = times[:]
        pontosGrupo = pontos[:]
        order_map(timesGrupo, pontosGrupo, 1)
        if not lightSpeed and not fim:
            print()
            for i in range(len(grupo)):
                print("{}:\t{:.0f} pts ->\t{}".format(i+1,pontosGrupo[i],timesGrupo[i]))
        if fim:
            index = findIndex(timesGrupo[0])
            if not lightSpeed:
                print(timesGrupo[0],"EH {} CAMPEA{}!".format(vogal[index].upper(), gramaticaCampeao[index].upper()))
            else:
                #for i in range(len(grupo)):
                    #print("{}:\t{:.0f} pts ->\t{}".format(i+1,pontosGrupo[i],timesGrupo[i]))
                vezesCampeao[index] += 1
                for ponto in range(len(times)):
                    mediaPontos[ponto] += pontos[ponto]
    except Exception as e:
        print(e)

def playGrupo(grupo, pontos):
    for turno in range(2):
        teamsNum = len(times)
        teamHome = 0
        teamAway = teamsNum - 1
        teamHomeM1 = teamsNum - 1
        teamAwayM1 = teamsNum - 1
        jogosCasa = []
        for i in range(len(times)):
            jogosCasa.append(0)
        for i in range(len(times)-1):
            if i and not lightSpeed:
                input("Pressione ENTER para continuar...")
            if not lightSpeed:
                print("\nRodada {}:".format(i+1+19*turno))
            for j in range(int(len(times)/2)):
                if j == int(len(times)/2)-1:
                    lastGame = True
                else:
                    lastGame = False
                if not j:
                    x = 0
                else:
                    x = teamHome
                if jogosCasa[x] <= jogosCasa[teamAway]:
                    if turno:
                        match(pontos, mediaPontos, times[teamAway], times[x], grupo, False, False, lastGame)
                    else:
                        match(pontos, mediaPontos, times[x], times[teamAway], grupo, False, False, lastGame)
                    jogosCasa[x] += 1
                else:
                    if turno:
                        match(pontos, mediaPontos, times[x], times[teamAway], grupo, False, False, lastGame)
                    else:
                        match(pontos, mediaPontos, times[teamAway], times[x], grupo, False, False, lastGame)
                    jogosCasa[teamAway] += 1
                teamHome += 1
                if teamHome > teamsNum - 1:
                    teamHome = 1
                teamAway -= 1
                if teamAway < 1: 
                    teamAway = teamsNum - 1
            teamHomeM1 -= 1
            teamAwayM1 -= 1
            teamHome = teamHomeM1
            teamAway = teamAwayM1
            if not lightSpeed:
                print("\nFim da rodada {}!".format(i+1+19*turno))

def main():
    if lightSpeed:
        while True:
            numSimuls = input("Quantas simulacoes rodar? ")
            try:
                numSimuls = int(numSimuls)
                if numSimuls > 0:
                    inicio = time()
                    break
                else:
                    print("Valor invalido! Tente novamente...")
            except:
                print("Valor invalido! Tente novamente...")
        
    else:
        numSimuls = 1

    for i in range(numSimuls):
        pontos = []
        for i in times:
            pontos.append(0)
        if a%((numModos+1)/2) < (numModos-1)/2:
            if not lightSpeed:
                print("Comeca o campeonato!\n")

            playGrupo(times, pontos)

            showTable(pontos, mediaPontos, times, True)
        else:
            while True:
                while True:
                    time1 = input("time 1: ")
                    if time1.upper() in times or time1 == '':
                        break
                    else:
                        print("Reposta invalida! Tente novamente...")
                if time1 == '':
                    break
                while True:
                    time2 = input("time 2: ")
                    if time2.upper() in times or time2 == '':
                        break
                    else:
                        print("Reposta invalida! Tente novamente...")
                if time2 == '':
                    break
                while True:
                    neutro = input("Mando de campo [0] | Campo neutro [1]:\n")
                    if neutro == '1':
                        neutro = True
                        break
                    elif neutro == '0':
                        neutro = False
                        break
                    else:
                        print("Valor invalido! Tente novamente...")
                match(pontos, mediaPontos, time1, time2, times, neutro, True)

    if lightSpeed and not amistoso:
        aux = times[:]
        for i in range(len(times)):
            mediaPontos[i] /= (numSimuls*1.0)
        order_map(times, vezesCampeao, 1)
        order_map(aux, mediaPontos, 1)
        print("Numero de Simulacoes realizadas: {}\nTempo de execucao: {:.2f} segundos".format(numSimuls, time() - inicio))
        print("Media de gols por jogo: {:.3f}".format(gols/(jogos*1.0)))
        for i in range(len(times)):
            #if debug:
                #debugMessage = '\t\t[DEVERIA SER: ' + str(meta[i]*numSimuls/10000.0) + ']'
            #else:
            debugMessage = ''
            print("{}:\t{}x campeao ->\t{} {}".format(i+1, vezesCampeao[i], times[i], debugMessage))
        print()
        for i in range(len(times)):
            print("{}:\t{:.0f} pts ->\t{}".format(i+1, mediaPontos[i], aux[i]))
if __name__ == '__main__':
    main()