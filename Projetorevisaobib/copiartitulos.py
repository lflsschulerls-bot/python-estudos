import requests, bs4

res = requests.get('https://repositorio.ufpe.br/handle/123456789/25413/simple-search?location=123456789%2F25413&query=&filter_field_1=dateIssued&filter_type_1=equals&filter_value_1=2025&rpp=40&sort_by=dc.date.issued_dt&order=DESC&etal=0&submit_search=Atualizar')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

# A lista é uma tabela, encontre <td> e headers="t2" para título e headers='t3' para autor
linhas = soup.find_all('tr')

listaDissertacoes = []

for linha in linhas:
    celulasTitulos = soup.find('td', headers='t2')
    celulaAutores = soup.find('td', headers='t3')

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