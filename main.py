import json
import os
from src.scraper import buscar_preco_produto
from src.database import salvar_historico
from src.notifier import disparar_alerta

CAMINHO_JSON = "produtos.json"

def carregar_produtos():
    """Carrega a lista de produtos do arquivo JSON de forma segura."""
    if not os.path.exists(CAMINHO_JSON):
        print(f"❌ Arquivo {CAMINHO_JSON} não encontrado!")
        return []
        
    with open(CAMINHO_JSON, "r", encoding="utf-8-sig") as f:
        return json.load(f)

def main():
    print("Iniciando varredura da lista de produtos...\n")
    
    produtos = carregar_produtos()
    
    if not produtos:
        print("Nenhum produto cadastrado para monitorar.")
        return

    # Loop para passar por cada produto da lista
    for item in produtos:
        nome = item["nome"]
        url = item["url"]
        preco_limite = item["preco_limite"]
        
        print(f"🔍 Verificando: {nome}...")
        
        preco_atual = buscar_preco_produto(url)
        
        if preco_atual is not None:
            print(f"   -> Preço atual: R$ {preco_atual} (Meta: R$ {preco_limite})")
            
            # Salva no histórico (se quiser separar por produto no CSV depois, podemos evoluir)
            salvar_historico(preco_atual)
            
            # Dispara o alerta se atingiu a meta
            disparar_alerta(preco_atual, preco_limite)
        else:
            print(f"   -> ⚠️ Falha ao capturar o preço para este produto.")
            
        print("-" * 40)

if __name__ == "__main__":
    main()