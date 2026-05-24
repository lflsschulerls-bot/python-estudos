## projeto prático

def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

continuar = '1'
while continuar == '1':
    print('digite um número inteiro: ')
    try:
        numeroEscolhido = int(input())

    except ValueError:
        print('Erro: Digite um número inteiro válido')
        continue

    while True:
        calculo = collatz(numeroEscolhido)
        numeroEscolhido = calculo
        print(calculo)
        if calculo == 1:
            numeroEscolhido = None
            break
    continuar = input('Gostaria de fazer uma nova sequência? (1=Sim) (2=Não)')
    if continuar == '1':
        continue
    else:
        break