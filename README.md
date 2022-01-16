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

## Programação 
A programação é realizada com uma sequência de comandos separados por ponto e vírgula ";"

Por exemplo: 
* TRS;ESQ;FRT;ESQ;FRT;ESQ;FRT;ESQ;FRT;PAR


## Configuração GPIOs 

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


