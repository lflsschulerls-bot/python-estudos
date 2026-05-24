## Jogo de adivinhação ##
mensagem1 = 'Prezado(a), seja bem vindo(a) ao jogo de adivinhação'
mensagem2 = 'Qual o seu nome?'


print(mensagem1)
print(mensagem2)
seuNome = input()

while True:
    mensagem3 = 'Certo ' + seuNome + ' se prepare para a pergunta do milênio: O que é O que é, tem 4 pernas mas não anda?'
    print(mensagem3)
    resposta = input()
    if resposta == 'cadeira':
        print('Está quase lá')
        continue
    elif resposta != 'mesa':
        print('Errou feio! errou rude')
        continue
    elif resposta == 'mesa':
        print('arrasou!')
    break

        
