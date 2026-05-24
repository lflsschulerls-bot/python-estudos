# Adivinhar o número

import random
import sys

continuar = '1'
while continuar == '1':
    print('Estou pensando em um número entre 1 a 20')
    numeroSecreto = random.randint(1, 20)

    # Pedir para o jogador adivinhar 6 vezes no máx
    for tentativas in range(1, 7):
        print('Tente adivinhar')
        guess = int(input())

        if guess < numeroSecreto:
            print('Sua tentativa foi baixa')
        elif guess > numeroSecreto:
            print('Sua tentativa foi muito alta')
        else:
            break #Esta condição corresponde a resposta certa

    if guess == numeroSecreto:
        print('Bom trabalho! Você acertou meu número')
    else:
        print('Que peninha, mais sorte da próxima vez. O número que pensei foi ' + str(numeroSecreto))
    continuar = input('Gostaria de continuar? (1=vamos) (2=não)')
    if continuar != '1':
        sys.exit()
