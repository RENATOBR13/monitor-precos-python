import os
import csv
from datetime import datetime

ARQUIVO_HISTORICO = "historico_precos.csv"

def salvar_historico(preco: float):
    """Salva a data, hora e o preço coletado em um arquivo CSV local."""
    arquivo_existe = os.path.exists(ARQUIVO_HISTORICO)
    
    with open(ARQUIVO_HISTORICO, mode='a', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        if not arquivo_existe:
            escritor.writerow(["Data/Hora", "Preço (R$)"])
        escritor.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), preco])