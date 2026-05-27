coisas = {'Corda': 1,
             'Tocha': 6,
             'Moeda de ouro': 42,
             'Adaga': 1,
             'Flechas': 12
}

def displayInventory(inventory):
    print('inventário:')
    totalItens = 0
    for k, v in inventory.items():
        print(str(inventory[k]) + 'x ' + k)
        totalItens += v
    resultado = "Número total de itens é: " + str(totalItens)
    return resultado

## Despojos do dragão
dragonLoot = ['Moeda de ouro', 'Adaga', 'Moeda de ouro', 'Moeda de ouro', 'Rubi']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        # Se o item não existir no inventário, define como 0 e soma 1
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


inv = addToInventory(coisas, dragonLoot)
displayInventory(coisas)