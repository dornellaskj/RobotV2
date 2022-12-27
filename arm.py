import power
import megaio
import time

ELBOW = 32
SHOULDER = 1
class Base:
    def __move(direction, part, time):
        if direction == 1:
            power.forward()
        if direction == 0:
            power.backward()
        megaio.set_relays(0, part)
        time.sleep(time)
        power.off()

class Arm(Base):
    def __init__(self):
        Base.__init__(self)
        
    def shoulder_up(time):
        self.__move(1, SHOULDER, time)
    