import json
import os

CAMINHO_JSON = "produtos.json"

def adicionar_novo_produto():
    print("=== 📦 Cadastro de Novo Produto no Monitorador ===")
    
    nome = input("Digite o nome do produto: ").strip()
    url = input("Cole a URL do produto: ").strip()
    
    try:
        preco_limite = float(input("Digite o preço limite (ex: 50.00): ").replace(",", "."))
    except ValueError:
        print("❌ Preço inválido! Use apenas números (ex: 45.90).")
        return

    produtos = []
    if os.path.exists(CAMINHO_JSON):
        with open(CAMINHO_JSON, "r", encoding="utf-8-sig") as f:
            try:
                produtos = json.load(f)
            except json.JSONDecodeError:
                produtos = []

    novo_item = {
        "nome": nome,
        "url": url,
        "preco_limite": preco_limite
    }
    produtos.append(novo_item)

    with open(CAMINHO_JSON, "w", encoding="utf-8") as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)

    print(f"\n✅ Produto '{nome}' cadastrado com sucesso no arquivo produtos.json!")

if __name__ == "__main__":
    adicionar_novo_produto()
