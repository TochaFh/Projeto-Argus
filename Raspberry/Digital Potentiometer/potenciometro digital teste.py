import RPi.GPIO as GPIO
import time
from digitalPotentiometer import DigitalPotentiometer

GPIO.setmode(GPIO.BCM)
#BUTTON = 5
#GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# INC_PIN, UD_PIN
print("inicio")
pd = DigitalPotentiometer(5, 6)
time.sleep(5)

pd.stepUp(100)

for i in range(1, 100):
    pd.stepDown(1)
    print("down " + str(i))
    time.sleep(1)