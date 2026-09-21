from machine import Pin
from time import sleep

led_verde = Pin(15, Pin.OUT)
led_amarelo = Pin(14, Pin.OUT)
led_vermelho = Pin(13, Pin.OUT)

LIMITE_AUTORIZADA = 2000
LIMITE_REDUZIDA = 200


def apagar_leds():
    led_verde.value(0)
    led_amarelo.value(0)
    led_vermelho.value(0)


def mostrar_representacao(valor):
    valor16 = valor & 0xFFFF
    print("Representacao da energia disponivel:")
    print("  Decimal:     ", valor)
    print("  Binario:     ", bin(valor16))
    print("  Hexadecimal: ", hex(valor16))


def verificar_recarga(geracao, consumo):
    disponivel = geracao - consumo

    if disponivel >= LIMITE_AUTORIZADA:
        status = "RECARGA AUTORIZADA"
    elif disponivel >= LIMITE_REDUZIDA:
        status = "RECARGA REDUZIDA"
    else:
        status = "RECARGA BLOQUEADA"

    apagar_leds()
    if status == "RECARGA AUTORIZADA":
        led_verde.value(1)
    elif status == "RECARGA REDUZIDA":
        led_amarelo.value(1)
    else:
        led_vermelho.value(1)

    print("--------------------------------------------------")
    print("GERACAO:", geracao, "W")
    print("CONSUMO:", consumo, "W")
    print("DISPONIVEL:", disponivel, "W")
    print("STATUS:", status)
    mostrar_representacao(disponivel)


situacoes = [
    (4000, 1500),
    (1800, 1500),
    (1000, 1800),
]

print("Sistema de controle de recarga iniciado")

while True:
    for geracao, consumo in situacoes:
        verificar_recarga(geracao, consumo)
        sleep(3)
