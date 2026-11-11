from src.scraper import buscar_preco_produto
from src.database import salvar_historico
from src.notifier import disparar_alerta

# URL de um livro de teste no site Books to Scrape
URL_ALVO = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
PRECO_LIMITE = 60.00  # Como o livro custa cerca de 51.77, o alerta vai disparar avisando que está abaixo da meta!

def main():
    print("Iniciando varredura do produto de teste...")
    
    preco_atual = buscar_preco_produto(URL_ALVO)
    
    if preco_atual is not None:
        print(f"Preço capturado com sucesso: R$ {preco_atual}")
        salvar_historico(preco_atual)
        
        # Se quiser testar o WhatsApp real, substitua pelo seu número. 
        # Se quiser testar só o console por enquanto, a função anterior de console serve perfeitamente.
        MEU_TELEFONE = "+5511982647732"  # Coloque seu número real com DDD
        disparar_alerta(preco_atual, PRECO_LIMITE)
    else:
        print("Falha ao capturar o preço nesta execução.")

if __name__ == "__main__":
    main()