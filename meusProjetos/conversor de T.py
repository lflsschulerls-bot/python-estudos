## Conversor de temperatura babadeiro

# Mensagens
m1 = 'Bem-vinde a calculadora babadeira. Escolha qual a conversão desejada: '
m2 = '1 - Celsius para Kelvin'
m3 = '2 - Kelvin para Celsius'
m4 = '3 - Celsius para Fahrenheit'
m5 = '4 - Fahrenheit para Celsius'
m6 = 'Insira o valor em Celsius: '
m7 = 'Insira o valor em Kelvin: '
m8 = 'Insira o valor em Fahrenheit: '

def celsiuspFahrenheit(valorCF):
    return str(round(((valorCF *(9/5))+32), 2)) + ' ºF'

def fahrenheitpCelsius(valorFC):
    return str(round(((valorFC-32)*(5/9)), 2)) + ' ºC'

def celsiuspKelvin(valorCK):
    return str(round((float(valorCK) + 273.15), 2)) + ' K'

def kelvinpCelsius(valorKC):
    return str(round((float(valorKC) - 273.15), 2)) + ' ºC'

while True:
    print(m1)
    print(m2)
    print(m3)
    print(m4)
    print(m5)
    escolha = input()
    if escolha == '1':
        print(m6)
        valorCK = input()
        print(celsiuspKelvin(valorCK))
    elif escolha == '2':
        print(m7)
        valorKC = input()
        print(kelvinpCelsius(valorKC))
    elif escolha == '3':
        print(m6)
        valorCF = input()
        valorCF = float(valorCF)
        print(celsiuspFahrenheit(valorCF))
    elif escolha == '4':
        print(m8)
        valorFC = input()
        valorFC = float(valorFC)
        print(fahrenheitpCelsius(valorFC))
    continuar = input('Gostaria de fazer uma nova conversãO? (1=Sim) (2=Não)')
    if continuar != '1':
        break
