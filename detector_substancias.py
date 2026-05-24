## Detector de substâncias
import random

# Mensagens
mensagens = ['Descubra se tal substância está no laboratório!', 'Seu score total é ', 'Seu saldo negativo é ',
            'Digite a substância. ', '(OBS: fórmula molecular, como exemplo H2O)', 'Parabéns, substância foi encontrada no laboratório. ',
            'Você ganhou um ponto. tente acertar mais vezes', 'Ih! Não temos essa substância aqui, meu caro. Vamos tentar de novo.',
            'Que pena, parece que você perdeu :( As substâncias restantes eram:', ' Gostaria de jogar novamente?', ' 1 - SIM   2 - NÃO',
            'Parabéns! Você ganhou o jogo '
            ]

# funções
def acertoSub(): #Função de acerto
    print(mensagens[5] + mensagens[6])
    subNoLab.remove(escolhaSub)
    global contador 
    contador += 1
    print(mensagens[1] + str(contador))
    print(mensagens[2] + str(scoreNeg))
def erroSub(): #Função de erro
    print(mensagens[7])
    global scoreNeg 
    scoreNeg -= 1
    print(mensagens[1] + str(contador))
    print(mensagens[2] + str(scoreNeg))

while True:
    susbtancias = ['H2SO4', 'HCl', 'NaCl', 'CuSO4', 'NaOH','ZnSO4', 'CuCl2']
    random.shuffle(susbtancias) #embaralhar subs.
    subNoLab = susbtancias[:3] #colher 3 primeiras substâncias da lista
    print(mensagens[0])
    contador = 0
    scoreNeg = 0
    while contador < 3 and scoreNeg > -5:
        print(mensagens[3])
        print(mensagens[4])
        escolhaSub = input()
        if escolhaSub in subNoLab: #acerto
            acertoSub()
        elif escolhaSub not in subNoLab: #erro
            erroSub()
    if contador == 3: #ganhou o jogo
        print(mensagens[-1])
    elif scoreNeg == -5: #perdeu o jogo — mostra substâncias restantes
        print(mensagens[8])
        print(subNoLab)
    print(mensagens[9])
    print(mensagens[10])
    continuar = input()
    if continuar != '1':
        break