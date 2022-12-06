''' Este script está configurado para ser executado no startup do sistema '''
import RPi.GPIO as GPIO
import time
import Config

try:
    Config.ledON()
    time.sleep(0.3)
    Config.ledOFF()
    time.sleep(0.2)
    Config.ledON()
    time.sleep(0.3)
    Config.ledOFF()
    time.sleep(0.2)
    Config.ledON()

    Config.threeBuzz()

    print("Programa iniciado")
    
finally:
    #GPIO.cleanup() comentado para o ledse manter aceso
    print('FIM Startup')