# Firmware URA IoT

## Comandos de Movimentação 

* FRT: anda para frente 
* ESQ: vira para esquerda em torno do próprio eixo 
* DIR: vira para direita em torno do próprio eixo 
* TRS: anda para trás 
* PAR: para o robô 
* FTT: anda para frente durante o tempo informado  
* EST: vira para esquerda em torno do próprio eixo durante o tempo informado  
* DRT: vira para direita em torno do próprio eixo durante o tempo informado 
* TRT: anda para trás durante o tempo informado 
* MTP: ajusta a 'potência' para cada motor com valores entre -100 à 100. No modo programação este comando precisa da especificação do tempo para concluir 

## Programação 
A programação é realizada com uma sequência de comandos separados por ponto e vírgula ";". Para identificar que é um programa a primeira instrução é 'PRG' 

Por exemplo: 
* PRG;TRS;ESQ;FRT;ESQ;FRT;ESQ;FRT;ESQ;FRT;PAR


## Configuração GPIOs 

### Ponte H 

| Ponte H L9110  | ESP32 |
| --------------- | --------------- | 
| B-1A | D5 |
| B-1B | D23 |
| G  | GND  | 
| VCC | Vin (5v) | 
| A-1A | D13 | 
| A-1B | D12 | 

### Sensor de distância (Ultrassom) 

| Sensor de distância | ESP32 |
| --------------- | --------------- | 
| GND | GND  | 
| Trig  | D19 | 
| Echo  | D18 |
| Vcc | 3.3v | 

### Sensores de Linha 

| Sensor de Linha Esquerdo | ESP32 |
| --------------- | --------------- | 
| G  | GND  | 
| V+ | 3.3v | 
| S  | D14 | 


| Sensor de Linha Direito | ESP32 |
| --------------- | --------------- | 
| G  | GND  | 
| V+ | 3.3v | 
| S  | D27 | 

## TODO

* Criar um comando para configurar a velocidade de referência de cada motor. Salvar essas velocidades em um arquivo de configuração  
* Melhoria: tratar quando vier com espaço antes do nome do comando 

## Concluídas 
* Implementar na classe controle de estados uma forma de receber um ou dois parâmentros para os comandos que precisarem 
