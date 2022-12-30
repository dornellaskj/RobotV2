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
    power.off()

def shoulder_up(move_time):
    __move(1, SHOULDER, move_time)
    