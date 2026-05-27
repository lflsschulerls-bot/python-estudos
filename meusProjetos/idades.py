idades = {'Luandson':'7 de Julho', 
          'Vanessa':'31 de janeiro',
          'Leonardo':'29 de Março',
          }

while True:
    print('Digite seu nome:')
    seuNome = input()
    if seuNome not in idades.keys():
        print('Não encontramos você. Gostaria de adicionar seu nome?')
        confirmacao = input('(s/n) ')
        if confirmacao == 's':
            print('Tudo perfeito. Qual sua idade? ')
            idades[seuNome] = input()
        else:
            print('Ok, até mais então')
    elif seuNome in idades.keys():
        print('Te encontramos! Seu aniversário é: ' + idades[seuNome])
    print('Gostaria de conferir ou adicionar outro nome? ')
    continuar = input('(s/n) ')
    if continuar != 's':
        print('Obrigado pela atenção')
        break