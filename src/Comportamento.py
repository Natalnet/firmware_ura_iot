import time 
class Comportamento:
    kind = 'Comportamento'
    def __init__ (self, _motores, _sensorLinhaEsq, _sensorLinhaDir):
        self.rodas = _motores
        self.sensorLinhaEsq = _sensorLinhaEsq
        self.sensorLinhaDir = _sensorLinhaDir 
        self.delta = 30 
        self.potenciaMaxima = 700
        self.potenciaLimiar = 500
        self.deltaMov = 15
        self.deltaGiro = 5
        self.movEsquerda = 0 
        self.movDireita = 0

    def seguirLinha(self): 
        time.sleep_ms(self.delta) 
        valorSLE = self.sensorLinhaEsq.value()
        valorSLD = self.sensorLinhaDir.value()
        if ( not valorSLD and not valorSLE ): 
            if (self.movDireita < self.potenciaLimiar):
                self.movDireita = self.potenciaLimiar
            if (self.movEsquerda < self.potenciaLimiar):
                self.movEsquerda = self.potenciaLimiar
            # iguala com a menor potencia 
            if (self.movDireita != self.movEsquerda):
                if (self.movDireita > self.movEsquerda):
                    self.movDireita = self.movEsquerda  
                else:
                    self.movEsquerda = self.movDireita
            if (self.movEsquerda < self.potenciaMaxima):
                self.movEsquerda = self.movEsquerda + self.deltaMov
            if (self.movDireita < self.potenciaMaxima):
                self.movDireita = self.movDireita + self.deltaMov 
            self.rodas.motores(self.movEsquerda,self.movDireita)
            return b'%s %d %d' % ("Frente!",self.movEsquerda,self.movDireita)
        elif (  valorSLD and  valorSLE ):
            if (self.movDireita > -self.potenciaLimiar):
                self.movDireita = -self.potenciaLimiar
            if (self.movEsquerda > -self.potenciaLimiar):
                self.movEsquerda = -self.potenciaLimiar
            # iguala com a menor ("maior negativametne") potencia 
            if (self.movDireita != self.movEsquerda):
                if (self.movDireita < self.movEsquerda):
                    self.movDireita = self.movEsquerda  
                else:
                    self.movEsquerda = self.movDireita                
            if (self.movEsquerda > -self.potenciaMaxima):
                self.movEsquerda = self.movEsquerda - self.deltaMov
            if (self.movDireita > -self.potenciaMaxima):
                self.movDireita = self.movDireita - self.deltaMov 
            self.rodas.motores(self.movEsquerda,self.movDireita)
            return b'%s %d %d' % ("Re!",self.movEsquerda,self.movDireita)
        elif ( valorSLD ):
            if (self.movDireita > -self.potenciaLimiar):
                self.movDireita = -self.potenciaLimiar
            if (self.movEsquerda < self.potenciaLimiar):
                self.movEsquerda = self.potenciaLimiar
            if (self.movEsquerda < self.potenciaMaxima):
                self.movEsquerda = self.movEsquerda + self.deltaGiro
            if (self.movDireita > -self.potenciaMaxima):
                self.movDireita = self.movDireita - self.deltaGiro
            self.rodas.motores(self.movEsquerda,self.movDireita)
            return b'%s %d %d' % ("Direito!",self.movEsquerda,self.movDireita)
        elif ( valorSLE ):
            if (self.movEsquerda > -self.potenciaLimiar ):
                self.movEsquerda = -self.potenciaLimiar 
            if (self.movDireita < self.potenciaLimiar):
                self.movDireita = self.potenciaLimiar
            if (self.movEsquerda > -self.potenciaMaxima):
                self.movEsquerda = self.movEsquerda - self.deltaGiro
            if (self.movDireita < self.potenciaMaxima):
                self.movDireita = self.movDireita + self.deltaGiro
            self.rodas.motores(self.movEsquerda,self.movDireita)
            return b'%s %d %d' % ("Esquerdo!",self.movEsquerda,self.movDireita)
            
