import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import time

motorL = 1 # Left motor pin
motorR = 7 # Right motor pin
sensor_pin = 2
i = 4.9 # the rate of time

while RPL.digitalRead(sensor_pin) == 1:
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
    time.sleep(0.3)
    if RPL.digitalRead(sensor_pin) != 1:
        break
# pauses then ends the while loop

while RPL.digitalRead(sensor_pin) == 0:
    move = time.time()
    while time.time() < (move + i):  # While the time is less than move + i, it will continue to move forward at a slower speed
        RPL.servoWrite(motorR, 1475)
        RPL.servoWrite(motorL, 1520)
    while time.time() > (move + i): # While the time is greater than move + i, it will stop
        RPL.servoWrite(motorR, 0)
        RPL.servoWrite(motorL, 0)
