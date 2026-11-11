def disparar_alerta(preco_atual: float, preco_limite: float):
    """Dispara o alerta quando o preço atinge a meta desejada."""
    if preco_atual <= preco_limite:
        print(f"🚨 ALERTA: O preço baixou para R$ {preco_atual}! (Meta: R$ {preco_limite})")
    else:
        print(f"ℹ️ Preço atual (R$ {preco_atual}) ainda está acima do limite (R$ {preco_limite}).")