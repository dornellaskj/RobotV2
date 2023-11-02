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
    arm.shoulderDown(1)
    arm.handClose(.4)
    arm.shoulderUp(1)
    arm.elbowDown(.3)

def putDown():
    arm.elbowUp(.4)
    arm.shoulderDown(1)
    arm.handOpen(.5)
    arm.shoulderUp(1)
    arm.elbowDown(.4)
    arm.handClose(.5)

def harper():
    pickUp()
    drive.forward(3.5)
    time.sleep(.2)
    drive.left(.2)
    time.sleep(.2)
    drive.forward(2.2)
    time.sleep(.2)
    drive.right(.3)
    time.sleep(.2)
    drive.forward(2)
    time.sleep(.2)
    putDown()

