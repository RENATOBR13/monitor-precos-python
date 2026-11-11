from datetime import datetime

# Tenta importar o pywhatkit de forma segura (caso não esteja instalado, o script não quebra)
try:
    import pywhatkit as kit
    PYWHATKIT_DISPONIVEL = True
except ImportError:
    PYWHATKIT_DISPONIVEL = False

TELEFONE_PADRAO = "+5511982647732"

def disparar_alerta(preco_atual: float, preco_limite: float, telefone_destino: str = TELEFONE_PADRAO):
    """
    Verifica se o preço atingiu a meta e dispara o alerta no console 
    e opcionalmente no WhatsApp (se a biblioteca estiver disponível).
    """
    if preco_atual <= preco_limite:
        mensagem = f"🚨 ALERTA DE PREÇO! O produto baixou para R$ {preco_atual} (Sua meta era R$ {preco_limite})."
        print(mensagem)
        
        if telefone_destino and PYWHATKIT_DISPONIVEL:
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
            print("ℹ️ Alerta registrado no console (Envio de WhatsApp desativado neste ambiente).")
    else:
        print(f"ℹ️ Preço atual (R$ {preco_atual}) ainda está acima do limite (R$ {preco_limite}).")