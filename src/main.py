# Reference to MQTT codes: https://RandomNerdTutorials.com

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub, server_port, mqtt_user, mqtt_password
  client = MQTTClient(client_id, mqtt_server, server_port, mqtt_user, mqtt_password)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

def sub_cb(topic, msg):
  global topic_sub, estadoAtual

  print((topic, msg))
  print(topic_sub)
  
  if len(msg) == 3:
    if topic == topic_sub and msg == b'FRT':
      print('Robô recebeu novo comando, frente')
      robot.passoFrente() 
      estadoAtual = 'PAR'
    elif topic == topic_sub and msg == b'PAR':
      print('Robô recebeu novo comando, parar')
      estadoAtual = 'PAR'
      robot.parar()  
    elif topic == topic_sub and msg == b'ESQ':
      print('Robô recebeu novo comando, esquerda')
      robot.passoEsquerda()
      estadoAtual = 'PAR'
    elif topic == topic_sub and msg == b'DIR':
      print('Robô recebeu novo comando, direita')
      robot.passoDireita()
      estadoAtual = 'PAR'
    elif topic == topic_sub and msg == b'TRS':
      print('Robô recebeu novo comando, ré')
      robot.passoRe() 
      estadoAtual = 'PAR'
    elif topic == topic_sub and msg == b'SLN':
      print('Robô recebeu novo comando, seguir linha')
      estadoAtual = 'SLN'
  if len(msg) > 3:

    # convert to string 
    dados = msg.decode('utf-8')

    coamandos = dados.split(';')
    if (coamandos[0] == 'PRG'):
      estadoAtual = 'PRG'
      #PRG;TRS;ESQ;FRT;ESQ;FRT;ESQ;FRT;ESQ;FRT;PAR 
      print("Execute program!")
      coamandos.pop(0)
      stateController.executePrograma(coamandos) 
    else: 
      comando = coamandos[0].split(" ")
      print(comando) 
      if (comando[0] == 'FTT'):
        print('Robô recebeu novo comando, frente por ',int(comando[1]),' ms') 
        robot.passoFrente(int(comando[1]))
        estadoAtual = 'PAR'
      elif (comando[0] == 'EST'):
        print('Robô recebeu novo comando, esquerda por ',int(comando[1]),' ms')
        robot.passoEsquerda(int(comando[1]))
        estadoAtual = 'PAR'
      elif (comando[0] == 'DRT'):
        print('Robô recebeu novo comando, direita por ',int(comando[1]),' ms')
        robot.passoDireita(int(comando[1]))
        estadoAtual = 'PAR'
      elif (comando[0] == 'TRT'):
        print('Robô recebeu novo comando, ré por ',int(comando[1]),' ms')
        robot.passoRe(int(comando[1]))
        estadoAtual = 'PAR'
      elif (comando[0] == 'MTP'):
        parametro1 = int(comando[1])*10
        parametro2 = int(comando[2])*10
        print('Robô recebeu novo comando, controle dos motores, direito para ',parametro1,' e esquerdo para ',parametro2)
        stateController.setCurrentState('MTP') 
        robot.motores(parametro1,parametro2) 
        estadoAtual = 'MTP'

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

contadorGeral = 0
respostaTerminal = ''
while True:
  try:
    client.check_msg()
    if estadoAtual == 'SLN':
      #print('seguindo linha!')
      respostaTerminal = comportamento.seguirLinha() 
      #time.sleep(1)
    else:
      stateController.updateExecution() 
    if (time.time() - last_message) >= message_interval:
      stateController.showState() 
      distance = distSensor.distance_cm()
      leftValue = leftLineSensor.value()
      rightValue = rightLineSensor.value()
      tempState = estadoAtual
      if estadoAtual == 'PRG':
        tempState = '%s:%s'%( 'PRG',stateController.getCurrentState()) 
      msg = b'MSG %d %d %d %d %s' % (contadorGeral,distance,leftValue,rightValue,tempState) 
      client.publish(topic_pub, msg)
      client.publish("URATESTE",b'%d %s'% (contadorGeral,respostaTerminal))
      respostaTerminal = ''
      last_message = time.time()
      contadorGeral += 1
  except OSError as e:
    restart_and_reconnect()




