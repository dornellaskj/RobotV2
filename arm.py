import power
import megaio


ELBOW = 32
SHOULDER = 1

def move(direction, part):
    if direction = 1:
        power.forward()
    if direction = 0:
        power.backward()
    megaio.set_relays(0, part)

def shoulder_up():
    move(1, SHOULDER)