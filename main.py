import talk
import time
import arm
import drive

def startup():
    talk.whoami()
    arm.shoulderUp(.3)
    arm.shoulderDown(.3)
    arm.elbowUp(.3)
    arm.elbowDown(.3)
    arm.wristUp(.3)
    arm.wristDown(.3)
    arm.handOpen(.3)
    arm.handClose(.3)
    drive.forward(.3)
    time.sleep(.2)
    drive.backward(.3)
    time.sleep(.2)
    drive.left(.3)
    time.sleep(.2)
    drive.right(.35)
