''' Este script está configurado para ser executado no startup do sistema '''
import RPi.GPIO as GPIO
import time
from motor import Motor

GPIO.setmode(GPIO.BCM)
HIGH = GPIO.HIGH
LOW = GPIO.LOW

MRight = Motor(23, 'd')
MLeft = Motor(24, 'e')

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
    
    for i in range(4):
        MRight.run()
        MLeft.stop()
        time.sleep(2)
        MRight.stop()
        MLeft.run()
        time.sleep(2)
        
    while 1:
        MRight.run()
        MLeft.run()
        time.sleep(5)
        MRight.stop()
        MLeft.stop()
        time.sleep(5)
    
    
finally:
    #GPIO.cleanup()
    print('FIM')
