import shutil, datetime

arquivoWord = r"C:\Users\usuario\OneDrive - Universidade Federal de Pernambuco\FACULDADE\Relatórios PIBID 2024-26\MODELORelatório_PIBID_LEONARDO_FERNANDO_DE_LEMOS_SCHULER.docx"
pastaDestino = r"C:\Users\usuario\OneDrive - Universidade Federal de Pernambuco\FACULDADE\Relatórios PIBID 2024-26\2026"

shutil.copy(arquivoWord, pastaDestino)