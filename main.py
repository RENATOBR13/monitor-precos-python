from src.scraper import buscar_preco_produto
from src.database import salvar_historico
from src.notifier import disparar_alerta

# Configurações do monitoramento
URL_ALVO = "https://exemplo.com/produto-ou-pagina"
PRECO_LIMITE = 100.00

def main():
    print("Iniciando varredura do produto...")
    
    preco_atual = buscar_preco_produto(URL_ALVO)
    
    if preco_atual is not None:
        print(f"Preço capturado com sucesso: R$ {preco_atual}")
        salvar_historico(preco_atual)
        disparar_alerta(preco_atual, PRECO_LIMITE)
    else:
        print("Falha ao capturar o preço nesta execução.")

if __name__ == "__main__":
    main()