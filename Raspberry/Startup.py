''' Este script está configurado para ser executado no startup do sistema '''
import RPi.GPIO as GPIO
import time
from motor import Motor
from test import teste_route_player

GPIO.setmode(GPIO.BCM)

ON_LED = 27
BUZZER = 22
GPIO.setup(ON_LED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT, initial=GPIO.LOW)

motorLeft = Motor(23, 'Esquerda')
motorRight = Motor(24, 'Direita')

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

    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(BUZZER, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(BUZZER, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(BUZZER, GPIO.LOW)

    print("Programa iniciado")
    teste_route_player(motorLeft, motorRight)

    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(BUZZER, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(BUZZER, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(BUZZER, GPIO.LOW)
    
finally:
    GPIO.cleanup()
    print('FIM')