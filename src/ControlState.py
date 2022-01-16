import time
class ControlState:
    kind = 'ControlState'
    def __init__(self, rb, dt):
        print("Control state started!")
        self.startTime = 0
        self.deltaTime = 0 
        self.state = 'PAR'
        self.defaultDelta = 500 
        self.instructionIndex = 0 
        self.instructions = [] 
        self.endExecution = False 
        self.robotControl = rb 
        # Este atributo guarda um dicionário relacionando nome do comando com 
        # o tempo para a sua execução 
        self.deltaTimeConf = dt 

    def initTimer(self, dt, st):
        self.startTime = time.ticks_ms()
        self.deltaTime = dt 
        self.state = st 

    def executePrograma(self, codes):
        self.instructions = codes
        self.endExecution = False 
        print(self.instructions) 
        self.initTimer(self.defaultDelta, self.instructions[0])
        self.robotControl.executaComando(self.instructions[0])
        self.showState() 

    def updateExecution(self): 
        #print(self.endExecution)
        if self.updateTimer() and not self.endExecution : 
            self.instructionIndex += 1 
            if self.instructionIndex < len(self.instructions):
                # atualiza a instrução atual 
                self.initTimer(self.deltaTimeConf[self.instructions[self.instructionIndex]], self.instructions[self.instructionIndex])
                #print("Atualizou: ",self.instructions[self.instructionIndex])
                self.robotControl.executaComando(self.instructions[self.instructionIndex])
                #print( self.deltaTimeConf[self.instructions[self.instructionIndex]] )
            else:
                self.instructionIndex = 0 
                self.state = 'FIM' 
                self.robotControl.executaComando('PAR')
                self.endExecution = True  


    def updateTimer(self): 
        if ( time.ticks_diff(  time.ticks_ms(), self.startTime) < self.deltaTime ):
            return False 
        else: 
            #self.state = 'PAR'
            return True 
    
    def showState(self):
        print(time.ticks_ms(), self.startTime, self.deltaTime, self.state, self.instructionIndex) 

    def getCurrentState(self):
        return self.state

    
