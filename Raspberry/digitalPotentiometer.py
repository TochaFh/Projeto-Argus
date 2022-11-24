class DigitalPotentiometer:
    def __init__(self, INC_PIN: int, UD_PIN):
        self.INC_PIN = INC_PIN
        self.UD_PIN = UD_PIN
    
    # value - de 0 a 100, inversamente proporcional à resistência
    # quanto maior o value, maior é a tensão da saída
    def setValue(self, value):
        return not self.invalid
    
    def getCommands(self):
        return self.commands