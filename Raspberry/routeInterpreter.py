commandDict = {
    'F': "FRENTE",
    'T': "TRAS",
    'E': "ESQUERDA",
    'D': "DIREITA",
    'P': "PARE",
    'C': "CAPTURAR",
    'X': "PAUSE"
}

class RouteInterpreter:
    def __init__(self, stringCode: str):
        self.stringCode = stringCode

        rawCommands = stringCode.split(',')
        commands = []
        self.invalid = False
        for i, com in enumerate(rawCommands):
            type = com[0]
            value = com[1:]

            if type not in commandDict.keys():
                self.errorMessage = "*RouteInterpreter: INVALID CODE - comando \"" + str(type) + "\" não existe -> no comando: \"" + str(com) + "\"  posição " + str(i + 1)
                self.invalid = True
                break
            if not value.isdigit():
                self.errorMessage = "*RouteInterpreter: INVALID CODE - valor \"" + str(value) + "\" não suportado -> no comando: \"" + str(com) + "\"  posição " + str(i + 1)
                self.invalid = True
                break

            commands.append(RouteCommand(type, int(value)))
            self.commands = commands
            self.length = len(commands)
            
    def isValid(self):
        return not self.invalid
    
    def getCommands(self):
        return self.commands

class RouteCommand:
    def __init__(self, type, value: int):
        self.type = type
        self.value = value
    def PRINT(self):
        print("- " + str(commandDict[self.type]) + ": " + str(self.value) + "  (" + str(self.type) + str(self.value) + ")")