import power
import megaio
import time

ELBOW = 32
SHOULDER = 1
HAND = 4
WRIST = 64


def __move(direction, part, move_time):
    if direction == 1:
        power.forward()
    if direction == 0:
        power.backward()
    megaio.set_relays(0, part)   
    time.sleep(move_time)
    #reverse power for a moment to stop movement
    if direction != 1:
        power.forward()
    if direction != 0:
        power.backward()
    time.sleep(.04)
    power.off()
    megaio.set_relays(0, 0)

def shoulderUp(move_time):
    __move(1, SHOULDER, move_time)

def shoulderDown(move_time):
    __move(0, SHOULDER, move_time)

def handOpen(move_time):
    if move_time > .5:
        move_time = .5
    __move(1, HAND, move_time)

def handClose(move_time):
    if move_time > .5:
        move_time = .5
    __move(0, HAND, move_time)

def wristUp(move_time):
    __move(1, WRIST, move_time)

def wristDown(move_time):
    __move(0, WRIST, move_time)

def elbowUp(move_time):
    __move(0, ELBOW, move_time)

def elbowDown(move_time):
    __move(1, ELBOW, move_time)

def pickUp():
    handOpen(.5)
    shoulderDown(1.2)
    handClose(.5)
    shoulderUp(1)

def putDown():
    shoulderDown(1.2)
    handOpen(.5)
    shoulderUp(1)
    handClose(.5)

    