## Contar palavras de um texto
print('Digite aqui o texto do aluno: ')
textoOriginal = input()
tudoMinusculo = textoOriginal.lower()
## Colhendo apenas as letras (incluindo espaços)
apenasLetras = ''.join([char for char in tudoMinusculo if char.isalpha() or char == ' '])
listaPalavras = apenasLetras.split() ## Juntando as palavras como itens na lista
qtdPalavras = {}
## Contando a qtd que cada palavra aparece
for item in listaPalavras:
    qtdPalavras.setdefault(item, 0)
    qtdPalavras[item] += 1
print('As quantidades foram: ')
totalPalavras = 0
for k, v in qtdPalavras.items():
    print(str(qtdPalavras[k]) + ' ' + k)
    totalPalavras += v