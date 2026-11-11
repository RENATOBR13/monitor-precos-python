import requests
from bs4 import BeautifulSoup

def buscar_preco_produto(url: str) -> float | None:
    """Faz a requisição na página web e extrai o preço atual."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    
    try:
        resposta = requests.get(url, headers=headers, timeout=10)
        resposta.raise_for_status()
        
        soup = BeautifulSoup(resposta.text, 'html.parser')
        
        # Ajuste a tag e a classe conforme o site que você for monitorar
        elemento_preco = soup.find("span", class_="preco-atual")
        
        if not elemento_preco:
            return None
        
        # Tratamento da string para converter em float
        preco_texto = (
            elemento_preco.get_text()
            .replace("R$", "")
            .replace(".", "")
            .replace(",", ".")
            .strip()
        )
        return float(preco_texto)
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return None