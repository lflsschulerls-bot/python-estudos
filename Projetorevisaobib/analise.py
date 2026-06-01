import pandas as pd
from collections import Counter


# 1. Lendo as 5 planilhas
df_2025 = pd.read_excel('dissertacoes_2025.xlsx')
df_2024 = pd.read_excel('dissertacoes_2024.xlsx')
df_2023 = pd.read_excel('dissertacoes_2023.xlsx')
df_2022 = pd.read_excel('dissertacoes_2022.xlsx')
df_2021 = pd.read_excel('dissertacoes_2021.xlsx') 

# 2. Juntando todas as linhas em uma única tabela
df_completo = pd.concat([df_2025, df_2024, df_2023, df_2022, df_2021], ignore_index=True)
df_completo.to_excel('dissertacoes_5anos.xlsx', index=False)

print(f"Sucesso! Temos um total de {len(df_completo)} dissertações para analisar.")

textao = ''.join(df_completo['titulo']).lower()
palavrasSemChar = ''.join([char for char in textao if char.isalpha() or char == ' '])
palavras = palavrasSemChar.split()

# Conectivos que queremos ignorar
stopwords = ['de', 'do', 'da', 'em', 'para', 'o', 'a', 'os', 'as', 'dos', 'das', 'uma', 'um', 'na', 'no', 'com', 'ao', 'à', ':', 'e',
             'por', 'nos'
             ]
palavras_limpas = [p for p in palavras if p not in stopwords]

bigramas = []
for i in range(len(palavras_limpas) - 1):
    termo = f"{palavras_limpas[i]} {palavras_limpas[i+1]}"
    bigramas.append(termo)

# Contando os termos mais frequentes
contador_termos = Counter(bigramas)
top_termos = contador_termos.most_common(15)

print("\n=== TOP 15 TERMOS CONCEITUAIS DOS ÚLTIMOS 5 ANOS ===")
for termo, freq in top_termos:
    print(f"{termo}: {freq} vezes")