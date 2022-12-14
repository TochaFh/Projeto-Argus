import RPi.GPIO as GPIO
import time

class Motor:
    def __init__(self, pin: int, name: str):
        self.pin = pin
        self.name = name
        
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)
        # Faz o relé interromper a alimentação do driver de motor
        # Isso faz o motor desativar
        GPIO.output(pin, GPIO.HIGH)

    def PRINT(self):
        print("- Motor: " + self.name + " - Inc Pin: " + str(self.dp.INC_PIN))
        
    #def setState(self, state: bool):
    #    GPIO.output(self.pin, state)

    def stop(self):
        GPIO.output(self.pin, GPIO.HIGH)
    
    def run(self):
        GPIO.output(self.pin, GPIO.LOW)