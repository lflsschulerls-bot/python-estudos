## Alguns elementos Químicos

elementos = {'C':'Carbono', 'H':'Hidrogênio', 'O':'Oxigênio', 'S':'Enxofre', 'Cl':'Cloro'}
print(elementos.keys())
print(elementos.values())
for k, v in elementos.items():
    print(k + ' -> ' + v)
parar = input()