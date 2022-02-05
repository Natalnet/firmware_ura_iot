import time
class ControlState:
    kind = 'ControlState'
    def __init__(self, rb, dtc):
        print("Controle de estado iniciado!")
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
        self.deltaTimeConf = dtc 

    def initTimer(self, dt, st):
        self.startTime = time.ticks_ms()
        self.deltaTime = dt 
        self.state = st 

    def executePrograma(self, codes):
        self.instructions = codes
        self.endExecution = False 
        print(self.instructions) 
        self.analisaEexecutaComando(0)
        self.showState() 

    def analisaEexecutaComando(self, indiceCmd):
        # Executa comandos 
        ## Comandos sem parâmetros                  
        # Atualiza a instrução atual 
        if len(self.instructions[indiceCmd]) == 3:
            self.initTimer(self.deltaTimeConf[self.instructions[indiceCmd]], self.instructions[indiceCmd])
            #print("Atualizou: ",self.instructions[indiceCmd])
            self.robotControl.executaComando(self.instructions[indiceCmd])
            #print( self.deltaTimeConf[self.instructions[indiceCmd]] )        
        elif len(self.instructions[indiceCmd]) > 3:
            print("Recebeu: ",self.instructions[indiceCmd])
            comando = self.instructions[indiceCmd].split(" ")
            if comando[0] == 'MTP':
                parametro1 = int(comando[1])*10
                parametro2 = int(comando[2])*10
                self.initTimer(int(comando[3]), comando[0]) 
                print('Parametros: ',parametro1,',',parametro2)
                print("Tempo: ", int(comando[3]))
                self.robotControl.motores(parametro1,parametro2) 
            ## Comandos com um parâmetro 
            else: 
                self.initTimer(int(comando[1]), comando[0]) 
                self.robotControl.executaComando(comando[0])
                print("Tempo: ", int(comando[1]))    

    def updateExecution(self): 
        #print(self.endExecution)
        if self.updateTimer() and not self.endExecution : 
            self.instructionIndex += 1 
            if self.instructionIndex < len(self.instructions):
                self.analisaEexecutaComando(self.instructionIndex)  
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

    def setCurrentState(self, _st):
        self.state = _st 

    
