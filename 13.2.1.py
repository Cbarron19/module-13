import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import time

motorL = 1
motorR = 7
sensor_pin = 2
i = 4.9

while RPL.digitalRead(sensor_pin) == 1:
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
    time.sleep(0.3)
    if RPL.digitalRead(sensor_pin) != 1:
        break

while RPL.digitalRead(sensor_pin) == 0:
    move = time.time()
    while time.time() < (move + i):
        RPL.servoWrite(motorR, 1475)
        RPL.servoWrite(motorL, 1520)
    while time.time() > (move + i):
        RPL.servoWrite(motorR, 0)
        RPL.servoWrite(motorL, 0)
