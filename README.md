# Sprint 3 - Controle Inteligente de Sessão de Recarga

Projeto da disciplina de Arquitetura de Computadores, inspirado no conceito
da GoodWe Smart Energy Controller.

## Integrantes
- Julia Junqueira Konishi RM:569506
- Miguel Putini RM:571624
- Alexandre Rizzi RM:569621
- João Giadans RM:571608
- João Scheren RM:568883

## O que o projeto faz

Simula um controlador que decide se uma sessão de recarga de veículo elétrico
pode ser autorizada, reduzida ou bloqueada, com base na diferença entre a
energia gerada e o consumo da residência. O resultado é mostrado em três LEDs
(verde, amarelo, vermelho) e no monitor serial.

## Como funciona

1. **Entrada**: valores de geração e consumo (simulados no código).
2. **Processamento**: `disponivel = geracao - consumo`, comparado com dois limites.
3. **Saída**: acende o LED correspondente e imprime os dados no terminal.

## Circuito

| LED | GPIO | Pino físico |
|---|---|---|
| Verde | GP15 | 20 |
| Amarelo | GP14 | 19 |
| Vermelho | GP13 | 17 |
| GND comum | GND | 18 |

Cada LED: GPIO → resistor 330 Ω → ânodo do LED → cátodo → GND.

## Como rodar

1. Acesse [wokwi.com](https://wokwi.com) e crie um projeto **MicroPython on
   Raspberry Pi Pico**.
2. Cole o conteúdo de `main.py` na aba de código.
3. Cole o conteúdo de `diagram.json` na aba de diagrama.
4. Clique em play e acompanhe o monitor serial.

## As três situações

| Situação | Geração | Consumo | Disponível | Status | LED |
|---|---|---|---|---|---|
| 1 | 4000 W | 1500 W | 2500 W | RECARGA AUTORIZADA | Verde |
| 2 | 1800 W | 1500 W | 300 W | RECARGA REDUZIDA | Amarelo |
| 3 | 1000 W | 1800 W | -800 W | RECARGA BLOQUEADA | Vermelho |

## Representação de dados

O valor da energia disponível é mostrado em decimal, binário e hexadecimal.
No caso negativo (-800 W), o valor é convertido para 16 bits com
`valor & 0xFFFF`, mostrando a representação em complemento de dois:

- Decimal: -800
- Binário: 0b1111110011100000
- Hexadecimal: 0xfce0


## Relação com Arquitetura de Computadores

- **Entrada/Saída**: os GPIOs do Pico como dispositivos de E/S mapeados em memória.
- **Processamento**: a subtração e as comparações rodam na CPU (ARM Cortex-M0+ do RP2040).
- **Memória**: o programa fica na flash; as variáveis, na RAM, enquanto o código executa.
- **Representação de dados**: o mesmo valor em decimal, binário e hexadecimal, e o uso de complemento de dois para números negativos.
