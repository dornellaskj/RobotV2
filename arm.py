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
    power.off()
    megaio.set_relays(0, 0)

def shoulderUp(move_time):
    __move(1, SHOULDER, move_time)

def shoulderDown(move_time):
    __move(1, SHOULDER, move_time)

def handOpen(move_time):
    __move(1, HAND, move_time)

def handClose(move_time):
    __move(1, HAND, move_time)

def wristUp(move_time):
    __move(1, HAND, move_time)

def wristDown(move_time):
    __move(1, HAND, move_time)

def ElbowUp(move_time):
    __move(1, HAND, move_time)

def ElbowDown(move_time):
    __move(1, HAND, move_time)
    