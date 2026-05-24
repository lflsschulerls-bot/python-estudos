## Calculadora de aprovação ##


continuar = '1'
while continuar == '1':
    print('Qual o nome do aluno?')
    nomeEstudante = input()
    print('Indique a média final:')
    mediaFinal = input() # Colocar a nota
    mediaFinal = float(mediaFinal)
    print('Qual a frequência?')
    freqEstudante= input()
    freqEstudante= float(freqEstudante)

    # Mensagens

    mensagem1 = nomeEstudante + '. Você foi reprovado por falta'
    mensagem2 = 'Parabéns ' + nomeEstudante + '. Você está aprovado com excelência.'
    mensagem3 = nomeEstudante + '. Você está aprovado por média'
    mensagem4 = 'Sua nota não alcançou a média esperada, porém você está elegível para a prova de recuperação'
    mensagem5 = 'Você foi reprovado por média'


    if freqEstudante < 75:
        print(mensagem1)
    elif mediaFinal >= 9 and freqEstudante>= 90:
        print(mensagem2)
    elif mediaFinal >= 9 and freqEstudante>= 75:
        print(mensagem3)
    elif 7 <= mediaFinal <= 8.9 and freqEstudante>= 75:
        print(mensagem3)
    elif 5 <= mediaFinal <= 6.9:
        print(mensagem4)
    else:
        print(mensagem5)
    continuar = input('Gostaria de cadastrar um novo estudante? (1=sim) (2=não)')
    if continuar == '2':
        break
print('Obrigado pela escolha!')
