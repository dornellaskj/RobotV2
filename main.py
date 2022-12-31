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
    drive.driveForward(.3)
    time.sleep(.1)
    drive.driveBackward(.3)
    time.sleep(.1)
    drive.turnLeft(.3)
    time.sleep(.1)
    drive.turnRight(.3)
