import time 
# Robot codes 
from L9110URA import L9110URA
robot = L9110URA(13,12,5,23)

robot.frente() 
time.sleep(1)
robot.frente(700) 
time.sleep(1)
robot.re() 
time.sleep(1)
robot.re(600) 
time.sleep(1)
robot.parar()
time.sleep(1)
robot.direita()
time.sleep(1)
robot.esquerda() 