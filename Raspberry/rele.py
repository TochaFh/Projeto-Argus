import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
R1 = 23
R2 = 24

GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)

GPIO.output(R2, GPIO.LOW)
print("hehe")
time.sleep(2)
GPIO.output(R2, GPIO.HIGH)
print("hehe")
time.sleep(5);
GPIO.output(R2, GPIO.LOW)
print("hehfe")