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
    drive.right(.34)

def pickUp():
    arm.handOpen(.5)
    arm.elbowUp(.4)
    arm.wristUp(.2)
    arm.shoulderDown(1)
    arm.handClose(.4)
    arm.shoulderUp(1)
    arm.wristDown(.2)
    arm.elbowDown(.3)

def putDown():
    arm.elbowUp(.4)
    arm.shoulderDown(1)
    arm.handOpen(.5)
    arm.shoulderUp(1)
    arm.elbowDown(.5)
    arm.handClose(.5)

def harper():
    pickUp()
    drive.forward(4)
    time.sleep(.2)
    drive.left(.1)
    time.sleep(.2)
    drive.forward(1.5)
    time.sleep(.2)
    drive.right(.5)
    time.sleep(.2)
    drive.forward(2.6)
    time.sleep(.2)
    putDown()

