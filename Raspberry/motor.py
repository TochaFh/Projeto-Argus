from digitalPotentiometer import DigitalPotentiometer

class Motor:
    def __init__(self, dp: DigitalPotentiometer, name: str):
        self.dp = dp
        self.name = name

    def PRINT(self):
        print("- Motor: " + self.name + " - Inc Pin: " + str(self.dp.INC_PIN))

    def stop(self):
        self.dp.setValue(0)
    
    def slow(self):
        self.dp.setValue(2)

    def regularSpeed(self):
        self.dp.setValue(7)

    def fast(self):
        self.dp.setValue(13)

    def move(self, speed: int):
        self.dp.setValue(speed)