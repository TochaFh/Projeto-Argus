import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIN_INC = 23
PIN_UD = 24
PIN_CS = 25
BUTTON = 5

HIGH = GPIO.HIGH
LOW = GPIO.LOW

GPIO.setup(PIN_INC, GPIO.OUT)
GPIO.setup(PIN_UD, GPIO.OUT)
GPIO.setup(PIN_CS, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    # -- LOOP --
    GPIO.output(PIN_CS, HIGH)
    GPIO.output(PIN_INC, HIGH)
    
    time.sleep(1)
    GPIO.output(PIN_CS, LOW)
    
    while 1:
        while GPIO.input(BUTTON) == LOW:
            print('not pressed')
            time.sleep(0.1)
            
        while GPIO.input(BUTTON) == HIGH:
            print('pressed 1')
            GPIO.output(PIN_UD, HIGH)
            time.sleep(0.01)
            GPIO.output(PIN_INC, LOW)
            time.sleep(0.01)
            GPIO.output(PIN_INC, HIGH)
            time.sleep(0.1)
            
        while GPIO.input(BUTTON) == LOW:
            print('not pressed')
            time.sleep(0.1)
            
        while GPIO.input(BUTTON) == HIGH:
            print('pressed 2')
            GPIO.output(PIN_UD, LOW)
            time.sleep(0.01)
            GPIO.output(PIN_INC, LOW)
            time.sleep(0.01)
            GPIO.output(PIN_INC, HIGH)
            time.sleep(0.1)
finally:
    GPIO.cleanup()
    print('FIM')