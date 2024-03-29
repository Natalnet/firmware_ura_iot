


# Complete project details at https://RandomNerdTutorials.com
from Comportamento import Comportamento
from umqttsimple import MQTTClient
import ubinascii
import machine
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

import time 

import json 
conf_file = open('conf.json') 
conf = json.load(conf_file) 
conf_file.close() 

dtTimeConfFile = open('dt_time.json')
dtTimeConf = json.load(dtTimeConfFile)
dtTimeConfFile.close() 

arquivoRoboConf = open('robo_conf.json') 
roboConf = json.load(arquivoRoboConf)
arquivoRoboConf.close() 


# Robot codes 
from L9110URA import L9110URA
robot = L9110URA(13,12,5,23)
robot.setVelocidades(roboConf['ref_vel_esq'], roboConf['ref_vel_dir']) 

estadoAtual = "PAR" 

from hcsr04 import HCSR04
 
distSensor = HCSR04(trigger_pin=19, echo_pin=18)

leftLineSensor =  machine.Pin(14, machine.Pin.IN,  machine.Pin.PULL_UP)
rightLineSensor =  machine.Pin(27, machine.Pin.IN,  machine.Pin.PULL_UP)

# Comportamentos 
## Seguidor de linha 
comportamento = Comportamento(robot,leftLineSensor,rightLineSensor)

# Control Robot State 
from ControlState import ControlState
stateController = ControlState(robot,dtTimeConf) 

ssid = conf["ssid"]
password = conf["password"]
mqtt_server = conf["mqtt_server"]
server_port = conf["server_port"] 
mqtt_user = conf["mqtt_user"]
mqtt_password = conf["mqtt_password"]

client_id = ubinascii.hexlify(machine.unique_id())

topic_sub = bytes(conf["topic_sub"], 'utf-8')
topic_pub = bytes(conf["topic_pub"], 'utf-8')

last_message = 0
message_interval = 1


station = network.WLAN(network.STA_IF)

station.active(True)

if not station.isconnected():

  print('Connecting to Wi-Fi...')

  station.connect(ssid, password)

  while not station.isconnected():
    pass

  print('Connected to Wi-Fi: ', station.ifconfig())








