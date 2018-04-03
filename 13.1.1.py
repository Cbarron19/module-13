import RoboPiLib as RPL
import setup

def motorStatus(x):
    if x == 1:
        RPL.servoWrite(0,2000)
        RPL.servoWrite(1,1000)
    if x == 0:
        RPL.servoWrite(0,0)
        RPL.servowrite(1,0)
