#! python3
import shutil, os, datetime

arquivoOriginal = r"C:\Users\usuario\OneDrive - Universidade Federal de Pernambuco\FACULDADE\Relatórios PIBID 2024-26\MODELORelatório_PIBID_LEONARDO_FERNANDO_DE_LEMOS_SCHULER.docx"
copia = r"C:\Users\usuario\OneDrive - Universidade Federal de Pernambuco\FACULDADE\Relatórios PIBID 2024-26\2026\relatorio_copia.docx"

shutil.copy(arquivoOriginal, copia)
print('Arquivo copiado com sucesso!')

# Renomear o arquivo
dataHoje = datetime.datetime.now()
mesHoje = dataHoje.strftime("%m")
anoHoje = dataHoje.strftime("%Y")
nomeArquivo = f"Relatório({mesHoje}.{anoHoje})_PIBID_LEONARDO_FERNANDO_DE_LEMOS_SCHULER.docx"
renomeado = os.path.join(r"C:\Users\usuario\OneDrive - Universidade Federal de Pernambuco\FACULDADE\Relatórios PIBID 2024-26\2026", nomeArquivo)
os.rename(copia, renomeado)
print('Arquivo renomeado com sucesso!')
finalizar = input()