import RPi.GPIO as GPIO
import time

class DigitalPotentiometer:
    def __init__(self, INC_PIN: int, UD_PIN):
        self.INC_PIN = INC_PIN
        self.UD_PIN = UD_PIN

        GPIO.setup(INC_PIN, GPIO.OUT)
        GPIO.setup(UD_PIN, GPIO.OUT)

        GPIO.output(INC_PIN, GPIO.HIGH)

        # deixa o potenciômetro em resistência máxima (tensão de saída = 0)
        # de acordo com os testes ele tem 31 passos !(??)
        self.stepDown(100)
        self.currentStep = 0
        print("Potenciometro digital inicializado - em 0")
    
    # value - de 0 a 100, diretamente proporcional à tensão de saída
    # quanto maior o value, menor é a resistência
    def setValue(self, value: int):
        stepsToValue = value - self.currentStep
        if stepsToValue > 0:
            self.stepUp(stepsToValue)
        else:
            self.stepDown(abs(stepsToValue))
        self.currentStep = value
        print("Set Value: " + str(value))

    def oneStepUp(self):
        GPIO.output(self.UD_PIN, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(self.INC_PIN, GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(self.INC_PIN, GPIO.HIGH)
        time.sleep(0.001)

    def oneStepDown(self):
        GPIO.output(self.UD_PIN, GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(self.INC_PIN, GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(self.INC_PIN, GPIO.HIGH)
        time.sleep(0.001)

    def stepUp(self, howManySteps):
        for i in range(howManySteps):
            self.oneStepUp()

    def stepDown(self, howManySteps):
        for i in range(howManySteps):
            self.oneStepDown()