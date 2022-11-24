import RPi.GPIO as GPIO
import time

class DigitalPotentiometer:
    def __init__(self, INC_PIN: int, UD_PIN):
        self.INC_PIN = INC_PIN
        self.UD_PIN = UD_PIN

        GPIO.setup(INC_PIN, GPIO.OUT)
        GPIO.setup(UD_PIN, GPIO.OUT)

        GPIO.output(INC_PIN, GPIO.HIGH)

        # zera o estado do potenciometro digital
        self.stepDown(100)
        self.currentStep = 0
    
    # value - de 0 a 100, inversamente proporcional à resistência
    # quanto maior o value, maior é a tensão da saída
    def setValue(self, value: int):
        stepsToValue = value - self.currentStep
        if stepsToValue > 0:
            self.stepUp(stepsToValue)
        else:
            self.stepDown(abs(stepsToValue))

    def oneStepUp(self):
        GPIO.output(self.UD_PIN, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(self.INC_PIN, GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(self.INC_PIN, GPIO.HIGH)
        time.sleep(0.1)

    def oneStepDown(self):
        GPIO.output(self.UD_PIN, GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(self.INC_PIN, GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(self.INC_PIN, GPIO.HIGH)
        time.sleep(0.1)

    def stepUp(self, howManySteps):
        for i in range(howManySteps):
            self.oneStepUp()

    def stepDown(self, howManySteps):
        for i in range(howManySteps):
            self.oneStepDown()