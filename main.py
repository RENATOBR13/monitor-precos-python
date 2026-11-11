import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import os

# Configurações básicas
URL_ALVO = "https://exemplo.com/produto-ou-pagina"  # Substitua por um site real de teste
PRECO_LIMITE = 100.00                              # Seu preço de alerta
ARQUIVO_HISTORICO = "historico_precos.csv"

def buscar_dados():
    """Faz a requisição na página web e retorna o objeto BeautifulSoup."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        resposta = requests.get(URL_ALVO, headers=headers)
        resposta.raise_for_status()
        return BeautifulSoup(resposta.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return None

def extrair_preco(soup):
    """Extrai o preço do HTML. (Ajuste o seletor conforme o site escolhido)"""
    # Exemplo genérico: procure a tag que contém o preço no site alvo
    elemento_preco = soup.find("span", class_="preco-atual")
    
    if not elemento_preco:
        return None
    
    # Tratamento da string de preço para converter em float (ex: "R$ 89,90" -> 89.90)
    preco_texto = elemento_preco.get_text().replace("R$", "").replace(".", "").replace(",", ".").strip()
    return float(preco_texto)

def salvar_historico(preco):
    """Salva a data, hora e o preço coletado em um arquivo CSV."""
    arquivo_existe = os.path.exists(ARQUIVO_HISTORICO)
    
    with open(ARQUIVO_HISTORICO, mode='a', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        if not arquivo_existe:
            escritor.writerow(["Data/Hora", "Preço (R$)"])
        escritor.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), preco])

def main():
    print("Iniciando varredura...")
    soup = buscar_dados()
    
    if soup:
        preco_atual = extrair_preco(soup)
        if preco_atual:
            print(f"Preço encontrado: R$ {preco_atual}")
            salvar_historico(preco_atual)
            
            if preco_atual <= PRECO_LIMITE:
                print("🚨 ALERTA: O preço baixou do limite desejado! Hora de comprar!")
                # Aqui você poderia adicionar uma função para enviar e-mail ou Telegram
            else:
                print("Preço ainda acima do limite.")
        else:
            print("Não foi possível localizar o elemento de preço na página.")

if __name__ == "__main__":
    main()