import sys

def addItemInventario():
        while True:
             item = input('Qual? ')
             inventario.append(item)
             print('adicionado com sucesso!')
             print('Quer adicionar outro item? (s/n)')
             escolha = input()
             if escolha == 's':
                  continue
             else:
                  break            
def remItemInventario():
        while True:
            item = input('Qual? ')
            if item not in inventario:
                 print('Ops, parece que esse item não se encontra')
            else:
                 inventario.remove(item)
                 print('Removido com sucesso')
            print('Quer remover outro item? (s/n)')
            escolha = input()
            if escolha == 's':
                continue
            else:
                break
def itemNoInventario():
        while True:
            itemEscolhido = input('Qual? ')
            if itemEscolhido in inventario:
                print('Sim, há este item aqui')
            else:
                print('Infelizmente você não possui ' + itemEscolhido)
            print('Quer conferir outro item? (s/n)')
            escolha = input()
            if escolha == 's':
                continue
            else:
                break

inventario = ['lã', 'papel', 'faca']

## Ação de abrir inventário
while True:
    print('Escolha a ação no inventário:')
    print('1 - Adicionar item')
    print('2 - remover item')
    print('3 - Conferir item')
    print('4 - Sair')
    escolha = input()
    if escolha == '1':
        addItemInventario()
    elif escolha == '2':
        remItemInventario()
    elif escolha == '3':
        itemNoInventario()
    elif escolha == '4':
         sys.exit()