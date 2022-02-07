import time 
class Comportamento:
    kind = 'Comportamento'
    def __init__ (self, _motores, _sensorLinhaEsq, _sensorLinhaDir):
        self.motores = _motores
        self.sensorLinhaEsq = _sensorLinhaEsq
        self.sensorLinhaDir = _sensorLinhaDir 
        self.delta = 60 
        self.motores.setVelocidades(700,700) 

    def seguirLinha(self): 
        time.sleep_ms(self.delta) 
        valorSLE = self.sensorLinhaEsq.value()
        valroSLD = self.sensorLinhaDir.value()
        if ( not valroSLD and not valorSLE ): 
            self.motores.frente()
            #print("Frente!")
        elif (  valroSLD and  valorSLE ):
            self.motores.re()
            #print("Re!")
        elif ( valorSLE ):
            self.motores.esquerda()
            #print("Esquerda!")
        elif ( valroSLD ):
            self.motores.direita()
            #print("Direita!") 
