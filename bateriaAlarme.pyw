import psutil
import time
from plyer import notification

# Função para enviar notificação
def notificar(titulo, mensagem):
    notification.notify(
        title=titulo,
        message=mensagem,
        timeout=5  # tempo da notificação na tela (segundos)
    )

# Estado anterior para não repetir notificação toda hora
estado_anterior = None

while True:
    bateria = psutil.sensors_battery()
    percent = bateria.percent
    carregando = bateria.power_plugged

    if carregando and percent >= 80 and estado_anterior != "carregando_alto":
        notificar("⚠️ Bateria cheia", "Desconecte o carregador (80%)")
        estado_anterior = "carregando_alto"

    elif not carregando and percent == 20 and estado_anterior != "descarregando_baixa":
        notificar("🔋 Bateria baixa", "Conecte o carregador (abaixo de 30%)")
        estado_anterior = "descarregando_baixa"

    elif (carregando and percent < 80) or (not carregando and percent > 30):
        estado_anterior = None  # reseta o estado

    time.sleep(60)  # verifica a cada 60 segundos
