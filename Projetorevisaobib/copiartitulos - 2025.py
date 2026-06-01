import pandas as pd
import requests, bs4

res = requests.get('https://repositorio.ufpe.br/handle/123456789/25413/simple-search?location=123456789%2F25413&query=&filter_field_1=dateIssued&filter_type_1=equals&filter_value_1=2025&rpp=40&sort_by=dc.date.issued_dt&order=DESC&etal=0&submit_search=Atualizar')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

# A lista é uma tabela, encontre <tr> a árvore principal
linhas = soup.find_all('tr')

listaDissertacoes = []

# Para cada linha da tabela, buscar título e autor
for linha in linhas:
    celulasTitulos = linha.find('td', headers='t2')
    celulaAutores = linha.find('td', headers='t3')

# Guardar título e autor
    if celulasTitulos and celulaAutores:
        tituloTexto = celulasTitulos.text.strip()
        autor = celulaAutores.text.strip()
        dissertacao = {"titulo": tituloTexto, 
                       "autor": autor,
                       "ano": 2025
        }
        listaDissertacoes.append(dissertacao)

print(f"Total de dissertações coletadas: {len(listaDissertacoes)}")
print(listaDissertacoes)

# Armazenar na planilha do excel
df = pd.DataFrame(listaDissertacoes)
df.to_excel('dissertacoes_2025.xlsx', index=False)
print(f"Pronto! {len(df)} dissertações foram salvas na planilha 'dissertacoes_2025.xlsx'.")