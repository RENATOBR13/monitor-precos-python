import requests
from bs4 import BeautifulSoup

def buscar_preco_produto(url: str) -> float | None:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        resposta = requests.get(url, headers=headers, timeout=10)
        resposta.raise_for_status()
        
        soup = BeautifulSoup(resposta.text, 'html.parser')
        
        # No site de teste Books to Scrape, o preço fica dentro de uma tag p com a classe 'price_color'
        elemento_preco = soup.find("p", class_="price_color")
        
        if not elemento_preco:
            print("⚠️ Tag de preço não encontrada na página.")
            return None
        
        # O texto vem no formato '£51.77'. Vamos limpar e converter para float.
        preco_texto = (
            elemento_preco.get_text()
            .replace("£", "")
            .replace("Â", "")  # Caractere especial de encoding comum em libras esterlinas
            .strip()
        )
        return float(preco_texto)
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return None