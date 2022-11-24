import RPi.GPIO as GPIO
import time
from digitalPotentiometer import DigitalPotentiometer

GPIO.setmode(GPIO.BCM)
BUTTON = 5
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# INC_PIN, UD_PIN
print("inicio")
pd = DigitalPotentiometer(5, 6)
time.sleep(2)

pd.stepDown(30)
print("down 29")
time.sleep(2)

pd.oneStepDown()
print("down")
time.sleep(2)

print("UP")
pd.oneStepUp()
time.sleep(2)

print("down")
pd.oneStepDown()
time.sleep(2)

print("down")
pd.oneStepDown()
time.sleep(2)

print("down")
pd.oneStepDown()
time.sleep(2)

print("UP")
pd.oneStepUp()
time.sleep(2)