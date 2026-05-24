def listaClassica(massas):
    massas = []
    while True:
        print('Insira um item na lista de massas: ' + str(len(massas)+1) + ' (ou aperte enter para parar)' )
        item = input()
        if item == '':
            break
        else:
            massas.append(item)
    texto = ''
    for i in range(len(massas)):
        if i == len(massas)-1:
            texto += massas[i]
        elif i == len(massas)-2:
            texto += massas[i] + ' e '
        else:
            texto += massas[i] + ', '
    return texto
massas = []
print(listaClassica(massas))