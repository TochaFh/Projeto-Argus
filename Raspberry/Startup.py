''' Este script está configurado para ser executado no startup do sistema '''
import RPi.GPIO as GPIO
import time
from motor import Motor
from test import teste_route_player

GPIO.setmode(GPIO.BCM)

ON_LED = 27
GPIO.setup(ON_LED, GPIO.OUT)

motorLeft = Motor(24, 'Esquerda')
motorRight = Motor(23, 'Direita')

try:
    # -- LOOP --
    GPIO.output(ON_LED, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(ON_LED, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(ON_LED, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(ON_LED, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(ON_LED, GPIO.HIGH)
    print("Programa iniciado")
    teste_route_player(motorLeft, motorRight)
    
finally:
    #GPIO.cleanup()
    print('FIM')