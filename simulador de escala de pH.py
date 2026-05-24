## Simulador de escala de pH

while True:
    pHi = int(input('digite o pH inicial: '))
    pHf = int(input('digite o pH final: '))

    for i in range(pHi, pHf + 1):
        print('pH é ->' + str(i))
        if i == 1 or i == 2 :
            print('Muito ácido')
        elif i == 3 or i == 4:
            print('Ácido')
        elif 5 <= i <= 6:
            print('Levemente ácido')
        elif i == 7:
            print('Neutro')
        elif 8 <= i <= 10:
            print('Levemente básico')
        elif i == 11 or i == 12:
            print('Básico')
        elif i == 13 or i == 14:
            print('Muito básico')
    continuar = input('Gostaria de refazer a escala? (1=Sim) (2=Não)')
    if continuar == '1':
        continue
    elif continuar == '2':
        break
