import RPi.GPIO as GPIO
from motor import Motor
import time

print("Configurando...")

GPIO.setmode(GPIO.BCM)

ON_LED = 27
BUZZER = 22
GPIO.setup(ON_LED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT, initial=GPIO.LOW)

motorLeft = Motor(23, 'Esquerda')
motorRight = Motor(24, 'Direita')

print("Configuração completa")

def ledON():
    GPIO.output(ON_LED, GPIO.HIGH)
def ledOFF():
    GPIO.output(ON_LED, GPIO.LOW)
    
def buzz(duration):
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(BUZZER, GPIO.LOW)
def threeBuzz():
    buzz(0.5)
    time.sleep(0.5)
    buzz(0.5)
    time.sleep(0.5)
    buzz(0.5)
    time.sleep(0.5)