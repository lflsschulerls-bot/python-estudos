## Calculadora de pH e pOH ##
import math

# Mensagens
m1 = 'Bem-vindo(a) a calculadora de pH e pOH'
m2 = 'primeiro, determine se o cálculo será de (1) pH ou (2) pOH:'
mpH1 = 'Insira um valor de concentração de Hidrônio. OBS: caso notação científica, use o formato em E, como 2e-3'
mpH2 = 'Seu valor de H+ é '
mpH3 = 'Agora calculando o pH dessa solução: '
mpOH1 = 'Insira um valor de concentração de Hidroxilas. OBS: caso notação científica, use o formato em E, como 2e-3'
mpOH2 = 'Seu valor de OH- é '
mpOH3 = 'Agora calculando o pOH dessa solução: '
mproblema = 'Acredito que ocorreu um problema! Escolha exatamente entre o número 1 ou 2 para efetuar o cálculo'
merro = 'Oh, parece que você digitou concentração como 0. Bom, não existe concentração nula. Volte ao início'
magradecer = 'Muito obrigado por usar a calculadora :)'

# Funções
def calculopH(valorH):
    return round(-math.log10(valorH), 2)
def calculopOH(valorOH):
    return round((-math.log10(valorOH)))


continuar = '1'
while continuar == '1':
    print(m1)
    print(m2)
    escolha= input()
    
    if escolha== '1':
        print(mpH1)
        valorH= input() # valor de H+
        valorH= float(valorH)
        if valorH == 0:
            print(merro)
        elif valorH > 0:
            print(mpH2 + str(valorH))
            print(mpH3 + str(calculopH(valorH)))
    elif escolha== '2':
        print(mpOH1)
        valorOH= input() # valor de OH-
        valorOH = float(valorOH)
        if valorOH == 0:
            print(merro)
        elif valorOH >0:
            print(mpOH2 + str(valorOH))
            print(mpOH3 + str(calculopOH(valorOH)))
    else:
        print(mproblema)

    continuar = input('Gostaria de fazer outro cálculo? (1=sim) (2=não)')
    if continuar == 'Não':
        break
print(magradecer)