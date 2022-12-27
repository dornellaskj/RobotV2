import power
import megaio
import time

ELBOW = 32
SHOULDER = 1
def __move(direction, part, time):
    if direction == 1:
        power.forward()
    if direction == 0:
        power.backward()
    megaio.set_relays(0, part)
    time.sleep(time)
    power.off()

def shoulder_up(time):
    __move(1, SHOULDER, time)
    