while True:
    print('Quem é você?')
    name = input()
    if name != 'João':
        print('Ihh, você não é o João')
        continue
    print('Oi, João. Qual é a senha? (é um peixinho)')
    password = input()
    if password == 'peixe-espada':
        break
print('Acesso liberado')
