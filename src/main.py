# Reference to MQTT codes: https://RandomNerdTutorials.com



def sub_cb(topic, msg):
  global topic_sub
  print((topic, msg))
  print(topic_sub)
  if len(msg) == 3:
    if topic == topic_sub and msg == b'FRT':
      print('ESP received, forward')
      robot.passoFrente() 
    elif topic == topic_sub and msg == b'PAR':
      print('ESP received, stop')
      robot.parar()  
    elif topic == topic_sub and msg == b'ESQ':
      print('ESP received,  turn left')
      robot.passoEsquerda()
    elif topic == topic_sub and msg == b'DIR':
      print('ESP received, turn right')
      robot.passoDireita()
    elif topic == topic_sub and msg == b'TRS':
      print('ESP received, backward')
      robot.passoRe() 
  if len(msg) > 3:
    print("Execute program!")
    print( type(msg) ) 
    # convert to string 
    data = msg.decode('utf-8')
    print(type(data))
    stateController.executePrograma(data)  


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

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
    stateController.updateExecution() 
    if (time.time() - last_message) >= message_interval:
      stateController.showState() 
      distance = distSensor.distance_cm()
      leftValue = leftLineSensor.value()
      rightValue = rightLineSensor.value()
      currentState = stateController.getCurrentState() 
      msg = b'MSG %d %d %d %d %s' % (counter,distance,leftValue,rightValue,currentState) 
      client.publish(topic_pub, msg)
      last_message = time.time()
      counter += 1
  except OSError as e:
    restart_and_reconnect()




