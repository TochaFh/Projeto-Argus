''' Este script está configurado para ser executado no startup do sistema '''
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
HIGH = GPIO.HIGH
LOW = GPIO.LOW

ON_LED = 27

GPIO.setup(ON_LED, GPIO.OUT)

try:
    # -- LOOP --
    GPIO.output(ON_LED, HIGH)
    time.sleep(0.3)
    GPIO.output(ON_LED, LOW)
    time.sleep(0.2)
    GPIO.output(ON_LED, HIGH)
    time.sleep(0.3)
    GPIO.output(ON_LED, LOW)
    time.sleep(0.2)
    GPIO.output(ON_LED, HIGH)
    print("Programa iniciado")
    
finally:
    #GPIO.cleanup()
    print('FIM')
