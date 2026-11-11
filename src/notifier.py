import pywhatkit as kit
from datetime import datetime

# Você pode definir um número padrão aqui para facilitar
TELEFONE_PADRAO = "+5511982647732"  # Substitua pelo seu DDD e número real

def disparar_alerta(preco_atual: float, preco_limite: float, telefone_destino: str = TELEFONE_PADRAO):
    """
    Verifica se o preço atingiu a meta e dispara o alerta no console 
    e opcionalmente no WhatsApp.
    """
    if preco_atual <= preco_limite:
        mensagem = f"🚨 ALERTA DE PREÇO! O produto baixou para R$ {preco_atual} (Sua meta era R$ {preco_limite})."
        print(mensagem)
        
        # Se um telefone de destino foi informado, tenta enviar o WhatsApp
        if telefone_destino:
            try:
                agora = datetime.now()
                hora = agora.hour
                minuto = agora.minute + 2
                
                if minuto >= 60:
                    minuto = 0
                    hora = (hora + 1) % 24

                print(f"Programando envio de WhatsApp para {telefone_destino}...")
                kit.sendwhatmsg(telefone_destino, mensagem, hora, minuto, wait_time=15)
                print("Mensagem programada com sucesso no WhatsApp!")
                
            except Exception as e:
                print(f"Erro ao tentar enviar o WhatsApp: {e}")
    else:
        print(f"ℹ️ Preço atual (R$ {preco_atual}) ainda está acima do limite (R$ {preco_limite}).")